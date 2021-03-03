path=[]

res=[]
def find(target, mykey):
    if isinstance(target, list):
        for index1,i in enumerate(target):
            path.append(index1)
            find(i,mykey)
    if isinstance(target, dict):
        for k, v in target.items():
            path.append(k)
            if k == mykey:
                res.append(path.copy())
            else:
                find(v,mykey)
    path.pop()

a=[
    {
        1:{
            2:3
        }
    },
    {
        "a":{
            "c":2
        }
    }
]
find(a,"c")
print(res)

# path = []
    #
    # res = []
    #
    # def mfind(target, mykey):
    #     if isinstance(target, list):
    #         for index1, i in enumerate(target):
    #             path.append(index1)
    #             mfind(i, mykey)
    #     if isinstance(target, dict):
    #         for k, v in target.items():
    #             path.append(k)
    #             if k == mykey:
    #                 res.append(path.copy())
    #             else:
    #                 mfind(v, mykey)
    #     if isinstance(target,lxml.etree._ElementUnicodeResult):
    #
    #         target=json.loads(str(target))
    #         if isinstance(target, dict):
    #             for k, v in target.items():
    #                 path.append(k)
    #                 if k == mykey:
    #                     res.append(path.copy())
    #                 else:
    #                     mfind(v, mykey)
    #         mfind(target,mykey)
    #     path.pop()
    # mfind(json_data,"hotList")
    # print(res)