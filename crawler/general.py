import os 

# Each page you crawl is a different project
def create_project_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Create queue and crawled files  ( if they don't exist yet )
def create_data_file(project_name, base_url):
    queue = project_name + 'queue.txt'
    crawled = project_name + 'crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Add data onto an existing file
def write_file(path, data):
    with open(path, 'w') as file:
        file.write(data)

# Append info to file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete the contents of file 
def delete_file_contents(path):
    with open(path, 'w'):
        pass

# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))

    return results

# Iterate through a set
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
        