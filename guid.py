import uuid

def new_guid():
    return str(uuid.uuid4()).replace('-','')

if __name__ == "__main__":
    print(new_guid())