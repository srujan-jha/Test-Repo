import getopt,sys
try:
    opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    if args[0] == "refs/heads/master":
        if not (args[1] == "refs/heads/nightly" or args[1] == "refs/heads/staging" or args[1] == "refs/heads/production"):
            sys.exit(1)
except getopt.GetoptError as err:
    print str(err)
    sys.exit(2)
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
