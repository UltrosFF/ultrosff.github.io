import requests as rq
import json
import os

WRFGS = {"pool_tag": "WRFGS","pool_id_bech_32":"pool1dmnyhw9uthknzcq4q6pwdc4vtfxz5zzrvd9eg432u60lzl959tw"}
SEA = {"pool_tag": "SEA","pool_id_bech_32":"pool17xh922cr9skc0fqk7sr8at6xx6eluh5qyv9p7ca2x0mtc3st0mz"}
A3C = {"pool_tag": "A3C","pool_id_bech_32":"pool1zkdaju2rjefa52uh6yh6etsxla0x6aqs6p6wm245y5szk7k3msd"}
BONE = {"pool_tag": "BONE","pool_id_bech_32":"pool1j742gcsul7u8c05rsqmkgpkvj5qadj0pew69nctu6crqy9wjjn4"}
CHEF = {"pool_tag": "CHEF","pool_id_bech_32":"pool1dqhaw0h2f4ehpdhh57quszcj22qhkglhg6yvaf39w3clxdl2kpy"}
FARM = {"pool_tag": "FARM","pool_id_bech_32":"pool1dpu6kslgxlg3ccrwxldl8e6r7ylnq0yalafmucp0yc7k6qegtt0"}
BAIDU = {"pool_tag": "BAIDU","pool_id_bech_32":"pool1c86ul4pnqvu7jzag8fjdy6dgrn6pt4ad4vmyq038hyg0wl2kaed"}
DDOS = {"pool_tag": "DDOS","pool_id_bech_32":"pool15k0zeppza4qzgf6z7wmwsgvl5rz9f6489zxhrxqa8dj6jzju6ct"}
ITZA = {"pool_tag": "ITZA","pool_id_bech_32":"pool1c2wa8326fulnkq42uerra78pue48pdwsqru2dhp5xrhsgzqmlsc"}
HAZEL = {"pool_tag": "HAZEL","pool_id_bech_32":"pool1h6q8jj55dn6727yydlypu0rz4sflf2enxhs0thqydmddgu3shl5"}
LIDO = {"pool_tag": "LIDO","pool_id_bech_32":"pool1kks6sgxvx7p6fe3hhnne68xzwa9jg8qgy50yt3w3lrelvns7390"}
ASPEN = {"pool_tag": "ASPEN","pool_id_bech_32":"pool1qku2yhky7sv4dfjfv42uyvauhehuqevk25aw952d7ulzqzx3jcu"}
PRIDE = {"pool_tag": "PRIDE","pool_id_bech_32":"pool1j099ctc7kcc9fa78dz5qwsy2g0n96lrgletwxvxmyzh4zd7ck0j"}
PSB = {"pool_tag": "PSB","pool_id_bech_32":"pool17taqml487n9t4r9a6ppvf9qv0qlw2lu4zcrzwfdsfcv6xp7uqym"}
PSYA = {"pool_tag": "PSYA","pool_id_bech_32":"pool1zytydvyy3qztrs8l2xyggvkfcjctp23m2hc3aj7sudnzgny79cg"}
QCPOL = {"pool_tag": "QCPOL","pool_id_bech_32":"pool1c2utlagkpht4zj0jetsf245c258geuxnjqp9kf4f2z9rutx9dz4"}
SALT = {"pool_tag": "SALT","pool_id_bech_32":"pool1a2gt2mvuf5zvtqlvw2xgks2efze3p4r985ft62q64lua7gx7lal"}
VEGAS = {"pool_tag": "VEGAS","pool_id_bech_32":"pool1df9rj4n0t3zlpak7xnh4ue6t3yh9zlw7a02w4l8askp77up25rt"}
WOOF = {"pool_tag": "WOOF","pool_id_bech_32":"pool1cg559cdc25fkvs73umj6w5nxlwy3mpmj02xt7p4v69eqs5ncz9k"}
RARE = {"pool_tag": "RARE","pool_id_bech_32":"pool1mscll7kd2y9c56kv7thv7kv99wjvrr72uwpmuhphaltjz0pkuqa"}
STOIC = {"pool_tag": "STOIC","pool_id_bech_32":"pool1pxw4z2m0lmw422hr32dwyy3uz9436g8p7qdmg2sl2w0m5pyk3yn"}
SCIFI = {"pool_tag": "SCIFI","pool_id_bech_32":"pool1lncn6a8xy3dm203m80hr4d4qm53h22a48e2s703z9qr9c20akka"}


pools = [WRFGS, STOIC,RARE,SALT, CHEF, QCPOL, ITZA, SEA, WOOF, DDOS, FARM, PSYA, PSB, A3C, BONE, PRIDE, VEGAS, HAZEL, BAIDU, LIDO, ASPEN]

stake_dict = {}

for pool in pools:
    bech_32 = pool["pool_id_bech_32"]
    response = rq.get("https://api.koios.rest/api/v0/pool_stake_snapshot?_pool_bech32="+bech_32).json()
    
    pool_stake = int(int(response[-1]['pool_stake'])//1000000)
    pool_tag = pool["pool_tag"]
    stake_dict[pool_tag] = pool_stake
    
pool_dict_list = []

value_getter = list(stake_dict.values())
value_getter.sort()
for stake in value_getter:
    for key,value in stake_dict.items():
        if stake == value:
            pool_dict_list.append({key: str(round(stake/1000000,2)) +" Mil. Ada"})
            
print(pool_dict_list)

ada_pools = {"ada_pools":pool_dict_list}

output_file_path = os.path.join("src", "outfile_ada_pools.json")

Path("src/outfile_ada_pools.json").unlink()

with open(output_file_path, "x") as outfile_ada_pools:
    json.dump(ada_pools, outfile_ada_pools)
