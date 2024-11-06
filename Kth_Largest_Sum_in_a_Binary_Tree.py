def removeSubfolders(folder):

    folder = sorted(folder)
    result = set()
    for x in folder:
        p = x.split("/")
        parent_dir = '111'
        for x in p[1:]:

            parent_dir += "/" + x
            if parent_dir in result:
                break
            else:
                result.add(parent_dir)


    return list(result)

print(removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])) # ["/a","/c/d","/c/f"]