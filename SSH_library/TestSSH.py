import paramiko
__version__ = '0.1'


class TestSSH:
    client = paramiko.SSHClient()
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'

    def login_to_host(self, ip, port, username, password):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=ip, port=port, username=username, password=password)

    def execute_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.readlines()

    def get_hostname(self):
        hostname = self.execute_command('hostname')
        output = (hostname[0]).strip()
        return output

    def get_network_configurations(self):
        network = self.execute_command('ifconfig')
        return "".join(network)

    def create_directory(self, dir_name):
        exist = self.directory_should_exist(dir_name)
        if exist == 1:
            sftp = self.client.open_sftp()
            sftp.rmdir(dir_name)
            sftp.close()
        sftp = self.client.open_sftp()
        sftp.mkdir(str(dir_name))
        sftp.close()
        return

    def directory_should_exist(self, dir_name):
        sftp = self.client.open_sftp()
        list_of_dirs = sftp.listdir()
        sftp.close()
        if dir_name in list_of_dirs:
            return 1
        else:
            return 0

    def file_should_exist(self, file_name):
        sftp = self.client.open_sftp()
        list_of_dirs = sftp.listdir()
        sftp.close()
        if file_name in list_of_dirs:
            return 1
        else:
            return 0

    def create_file(self, file_name, file_content, directory):
        self.execute_command('touch ' + str(directory).strip() + '/' + str(file_name))
        file = self.execute_command('echo ' + "\' " + str(file_content) + "\' >" + str(directory).strip() +
                                    '/' + str(file_name))
        return file

    def get_file(self, source, destination):
        sftp = self.client.open_sftp()
        sftp.get(source, destination)
        sftp.close()
        return

    def get_count_of_files(self, directory):
        sftp = self.client.open_sftp()
        count = sftp.listdir(directory)
        sftp.close()
        return len(count)

    def remove_file(self, file_name):
        sftp = self.client.open_sftp()
        sftp.remove(file_name)
        sftp.close()
        return

    def remove_files_in_directory(self, directory):
        directory = self.execute_command('rm ' + str(directory).strip() + '/*')
        return directory

    def put_file(self, source, destination):
        sftp = self.client.open_sftp()
        sftp.put(source, destination)
        sftp.close()
        return

    def logout_from_host(self):
        self.client.close()
        return
