import json
import os
import zipfile
import subprocess
import shutil
import getpass

try:
    from sch_cookie import sch_cookie
except ImportError:
    from .sch_cookie import sch_cookie


def create_directory_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)


def delete_files_under_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        create_directory_if_not_exist(folder_path)
    except:
        return 'Error while deleting files under folder %s' % folder_path
    else:
        return 'operation successful'


def read_json_file(file_path):
    for filename in os.listdir(file_path):
        # print('filename: ' + filename)
        if filename.endswith('.json'):
            with open(file_path + filename) as f:
                data = json.load(f)
                # print('reading of topology file is complete')
    return data


def write_json_file(topology_json, file_path, file_name):

    print(file_path + file_name)
    create_directory_if_not_exist(file_path)
    with open(file_path + file_name, 'w') as f:
        json.dump(topology_json, f)
        # print('updated file is written')


def update_params(topology_json, params):
    for i in range(len(topology_json['jobJsonList'])):
        obj = topology_json['jobJsonList'][i]['minimalJobJson']

        runtime_params = json.loads(obj['runtimeParameters'])
        for param in params:
            param_name = param
            param_new_value = params[param]

            if runtime_params.get(param_name, 'N/A') != 'N/A':
                runtime_params[param_name] = param_new_value
                obj['runtimeParameters'] = json.dumps(runtime_params)

    # print('topology is updated with parameters')
    return topology_json


def zip_file(src, dst):
    zf = zipfile.ZipFile("%s" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)

    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            if filename.endswith('.json'):
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                zf.write(absname, arcname)
    zf.close()


def import_topology(url, port, file_name, cookie):
    url_with_port = url if (port is "") else (url + ":" + port)
    request_url = url_with_port + '/topology/rest/v1/topologies/importTopologies?' \
                                     'updateMigrateOffsets=true&' \
                                     'updateNumInstances=true&' \
                                     'updateLabels=true&' \
                                     'updateRuntimeParameters=true'
    print('request_url: ' + request_url)
    import_command = """curl -X POST -F file=@%s '%s' --header "Content-Type:multipart/form-data" --header "X-Requested-By:SCH" --header "X-SS-REST-CALL:true" --header "X-SS-User-Auth-Token:%s" -v""" % \
                     (file_name, request_url,  cookie)
    print('import_command: ' + import_command)
    p1 = subprocess.Popen(import_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p1.communicate()
    return out, err


try:
    print('Please provide below information regarding Control Hub')
    target_sch_url = input('Control Hub URL (without port) :')
    target_sch_port = input('Control Hub Port :')

    target_sch_username = input('Control Hub Username :')
    target_sch_password = getpass.getpass('Control Hub Password :')

    print('Please provide below information for Event Hub')
    eventhub_uri = input('EventHub URI (example: DEV.servicebus.xxx.net:9093) :')
    eventhub_connection_string = input('EventHub Connection String :')
    eventhub_topic_name = input('EventHub Topic Name :')

    print('Please provide below information for Postgres')
    postgres_connection = input('Postgres Connection (this start with jdbc:postgresql://) :')
    postgres_username = input('Postgres Username :')
    postgres_password = getpass.getpass('Postgres Password: ')

    params = {}
    for i in ('eventhub_uri', 'eventhub_connection_string', 'eventhub_topic_name', 'postgres_connection', 'postgres_username', 'postgres_password'):
        params[i] = locals()[i]

    source_file_path = '../topology/'
    target_file_path = '../updated_topology/'
    file_name_json = 'topology.json'
    file_name_zipped = 'topology.zip'

    # Instantiate sch_cookie class & get the cookie for target control hub
    sch_cookie_inst = sch_cookie()
    target_cookie = sch_cookie_inst.get_cookie(target_sch_url, target_sch_port, target_sch_username, target_sch_password)
    if target_cookie == "":
        print('successfully connected to StreamSets Control Hub')
    else:
        print("Cannot connect to StreamSets Control Hub. Please check connection details.")
        raise Exception

    # Read source unzipped topology file
    source_topology = read_json_file(source_file_path)

    # Updated source topology with parameter mapping and create target topology topology
    topology_updated = update_params(source_topology, params)

    # Write target topology file to target folder
    write_json_file(topology_updated, target_file_path, file_name_json)

    # Zip the target topology file
    zip_file(target_file_path, target_file_path + file_name_zipped)

    # Import zipped target topology file into target control hub
    out, error = import_topology(target_sch_url, target_sch_port, target_file_path + file_name_zipped, target_cookie)

    # Delete files under updated_topology
    delete_files_under_folder(target_file_path)
    print('Congratulations, pipeline/topology is successfully created in StreamSets Control Hub')

except:
    print("There is an error. Please check your parameters")
