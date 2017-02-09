version="patch"
while 1:
    version = raw_input("Enter the version to be bumped(major/minor/patch)[default:patch]:")
    if not version:
        version = "patch"
        break
    else:
        if version == "minor" or version == "major" or version == "patch":
            break

f = open('version.xml', 'w')
f.write(version)
f.close()
print(version)
