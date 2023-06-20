import json
import requests as rq
import pprint as pp
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor
import time as t
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import requests_cache
#import blockfrost
#POLICIES

POLICY_ID="a5bb0e5bb275a573d744a021f9b3bff73595468e002755b447e01559"
POLICY_ID_2="ec77283fe87b1ccd7e5e8eb963de4c90abc8488e1e090b16b7f70a50"
POLICY_ID_S="de8086819da489257867042d568d4d7d4822387f94a092a578c40473"
POLICY_ID_SPECIAL= "dfdfc6dc2104fb78a54d942253439d86d550947307074eaa7e0de50c"





#POOLS_ID_AND_TRAITS

RARE = {'id': "dc31fffacd510b8a6accf2eecf59852ba4c18fcae383be5c37efd721",
        "pool": "RARE",
        "traits":
        ["Raccoon",
        "Red Panda",
        "Deep Purple",
         "Lunar New Year Red",
         "Escher",
         "Neon Gradient",
         "Halloween",
         "Beach",
         "Earth",
         "Web",
         "Film Noir",
         "Peace",
         "Glowing Pyramids",
         "Maffs",
         "Circles Animated",
         "Hosky Island",
         "Left Ring",
         "Solar Panels",
         "Spider Legs",
         "Dizzy",
         "Taco",
         "Shizzle",
         "Green Hat",
         "Light Blue Hat",
         "Not Megaman",
         "Orange Hoodie",
         "Spin Top Error",
         "Police Error",
         "Sweatband Error",
         "Bicycle Helmet Red",
         "Poo Cap",
         "Football Helmet",
         "Medicine Barrel",
         "Eyes Patched",
         "Dude",
         "Not A Red Turtle",
         "Not A Orange Turtle",
         "Not A Purple Turtle",
         "Not A Blue Turtle",
         "3D Glasses Error",
         "Black Lennons",
         "Orange Hazmat Suit",
         "Trick",
         "Good Boy"], "gnome_traits": ["wedontexisthaha"]}

STOIC = {'id': "099d512b6ffedd552ae38a9ae2123c116b1d20e1f01bb42a1f539fba",
        "pool": "STOIC",
        "traits":
        ['Robot',
        'Golden',
        'Space',
        'Fireworks lunar new year',
        'Race Track',
        'Starry Night',
        'Pink Gradient',
        'Orange Pink Gradient',
        'Antlers',
        'Eat Poo ',
        'Bandana',
        "Aye Cap'n",
        'Arrow',
        'Straw Hat',
        'Gold Poo Hat',
        'Neck Bolts',
        'Whatsthat',
        'Popped Eye',
        'Envy Eyes',
        'Sphinx Eyes',
        'Lightning Eyes',
        'Green Hazmat Suit',
        'Wen Animated',
        'Yeh But No',
        'Love', 'Rainbow Visor',
        'Upside Down Right Way Up'], "gnome_traits": ["not heard of yet"]}

HAZEL = {'id': 'be80794a946cf5e578846fc81e3c62ac13f4ab3335e0f5dc046edad4',
 'pool': 'HAZEL',
 'traits': 
['Oscar',
 'Charles Mask',
 'Glow In The Dark Skull',
 'Peach',
 'Wernis',
 'Epilogue',
 'Pernis',
 'Notepad',
 'Right Ring',
 'Handlebar Moustache',
 'McDonalds',
 'Sombrero',
 'Tea Cup',
 'Rob Boss',
 'McDonalds Error',
 'Captain Error',
 'Top Hat Red Error',
 'Crown Error',
 'Hero Error',
 'Poo Hat Error',
 'Hero 2 Error',
 'Gladiator Mask',
 '2st Place Medal',
 '1rd Chain',
 'Poo Bowtie',
 'Blue Bowtie',
 'Bubblebath',
 'Trash Can',
 'Overload',
 'Playing Card',
 '!%*@#?',
 'Crypto Ticker',
 'Blue Laser',
 'Eyepatch Right Error',
 'Upside Down Error',
 'Eyepatch Left Error',
 '3D Gloss Error',
 'Retro Rainbow Eyes',
 'Eyes Patched Error',
 'Thug Life Error',
 'Dude Error',
 'Love Error'],"gnome_traits": ['McHosky']}

LIDO = {'id': 'b5a1a820cc3783a4e637bce79d1cc2774b241c08251e45c5d1f8f3f6',
 'pool': 'LIDO',
 'traits':
['White',
 'Turtle',
 'Red',
 'Fireworks',
 'Pastel',
 'Salvador Hosky',
 'Bright Blue Green Gradient',
 'Biggie Hair',
 'Sick',
 'Bubblegum',
 'Top Hat Red',
 'Gold Ribbon Hat',
 'Pork Pie Hat',
 'Bicycle Helmet Orange',
 'Black and White Jester Neck',
 '1rd Place Medal',
 'Charles Eyes',
 'Grinch Eyes',
 'Were Eyes',
 'Ukraine Eyes',
 'Knitted Eyes',
 'Heterochromia',
 'Fish Bowl',
 'Traditional Painting',
 'Copper',
 'Cocktail',
 'Sticker',
 'Hosky Blocks',
 'Catastrophe',
 'Sad',
 'Zipped',
 'Visor Heart',
 'Goggles'],"gnome_traits": ['Poolception','Lobster']}

FIKA = {'id': 'f423b19715cca49029ed13ff02a110b63de7d96ad7a0536dc5887a41',
 'pool': 'FIKA',
 'traits': 
['Tiger Fur',
 'Gold Tiger',
 'Imagine Dragons',
 'Panda',
 'Clay Face',
 'Yellow',
 'Landscape',
 'FIAT',
 'Slate',
 'Press Start',
 'Field Gradient',
 'Stud Right',
 'Strawberry',
 'Trucker',
 'Bison',
 'Robin Hood Error',
 'Racing Helmet',
 'Black and White Jester',
 'Santa Hat Error',
 "Tea Cup World's Best Coder",
 'Black Mask',
 'Dumpling',
 'Trash Can',
 'Beatenup',
 'Astronaut',
 'Vegas Computer',
 'Another Holiday',
 'Sad-ish',
 'Robot Mouth',
 'Clown Mouth',
 'Snarl',
 'Lennon',
 'Asymmetrical Glasses'],"gnome_traits": ['Rug Merchant']}

CHEF = {'id': '682fd73eea4d7370b6f7a781c80b1252817b23f74688cea6257471f3',
 'pool': 'CHEF',
 'traits': 
['Bear',
 'Grey',
 'Blue',
 'Consensus 2022 Rare',
 'Black Radioactive Animated',
 'Underwater Animated',
 'Radioactive Yellow Animated',
 'Duplicate',
 'Bandaged Ear Left',
 'Pizza',
 'Bubblegum Popped',
 'Miner',
 'Black lunar new year hat',
 'Yellow Feather Hat',
 'Dune',
 'Rug Pool Bowl',
 'White Eyes',
 'Hoskasaur Eyes',
 'Hoskrogu Eyes',
 'Coyote Eyes',
 'Lunar New Year Gold',
 'Fools Gold',
 'Suits',
 'Joker',
 'Stamp',
 'Rug Me Daddy!',
 'Prison Bars',
 'NGMI',
 'Banksy Mouth',
 'Gherkin Mouth',
 'Gold Glasses',
 'Neistat'],"gnome_traits": ["Idiot"]}

VEGAS = {'id': '6a4a39566f5c45f0f6de34ef5e674b892e517ddeebd4eafcfd8583ef',
 'pool': 'VEGAS',
 'traits': 
['Radioactive Pink',
 'Banksy',
 'Cardano Whale',
 'Werewolf',
 'Ghost Chain',
 'Vegas Mask',
 'Baby Blue',
 'Lunar new year blue',
 'Vegas',
 'Underwater',
 'April Fools',
 'Neon Pink Gradient',
 'Mint Gradient',
 'Dizzy',
 'Cigarette',
 'Flat Peak',
 'Micky Error',
 'Blood Poo Error',
 'McDonalds Manager Error',
 'HoskyFett',
 'Squid Game Circle',
 'Holographic Hat Error',
 'Squid Game Square',
 'King Tutankhamun Error',
 'The Fools Hat',
 'Splitting Headache',
 'HBI Hat',
 'SlumDogeEx-Millionaire',
 'Jake Eyes',
 'Vasil Eyes',
 'Neon Sphinx Eyes',
 'Hosky Island Eyes',
 'Psychedelic Eyes',
 'Fairy Lights',
 'Meh',
 'Green Laser',
 'Heads-Up Display',
 'Late Night Glasses'],"gnome_traits": ['English']}

QCPOL = {'id': 'c2b8bff5160dd75149f2cae0955698550e8cf0d390025b26a9508a3e',
 'pool': 'QCPOL',
 'traits': 
['Hoskrogu',
 'Frankenhosk',
 'Sunset',
 'Morning Gradient',
 'Double Stud Right',
 'Cigar',
 'Captain',
 'Squid Game Square Error',
 'Squid Game Circle Error',
 'Squid Game Triangle Error',
 'Squid Game',
 'Third Ear Green',
 'Squid Game Error',
 'Pumpkin',
 'Pumpkin 2',
 'Red Collar',
 'Chain',
 'Crazy Eyes',
 'Pernis',
 'Think S#!tty',
 'Visor'],"gnome_traits": ['Cheshire']}

ITZA = {'id': 'c29dd3c55a4f3f3b02aae6463ef8e1e66a70b5d000f8a6dc3430ef04',
 'pool': 'ITZA',
 'traits': 
['Señor Josquí',
 'Flaming Hot',
 'Hosky Sticker',
 'Cerberosky',
 'Mint',
 'Full Moon',
 'Light Speed',
 'Gold Frameception',
 'Consensus 2022 Common',
 'GN',
 'Highly Classified',
 'GM',
 'Double Stud Left',
 'Burgundy Moustache',
 'Viking',
 'Elf Hat',
 'King Tutankhamun',
 'Silver Crown Error',
 'Miner Error',
 'Flat Peak Error',
 'Elf Hat Error',
 'Bandana Error',
 'Viking Error',
 'Top Hat Blue Error',
 'Party Hat',
 'Head Wrap',
 'Diamond Chain',
 'Robot Bowtie',
 'Green Poncho',
 'Knackered',
 'Silver',
 'Glass Jarsky',
 'Wen',
 'Laser Visor',
 'Yellow Laser Error',
 'Green Laser Error',
 'Back To The Future Error',
 'Red Laser Error',
 'Blue Laser Error',
 'Visor Animated',
 'Pilot Glasses Classic'],"gnome_traits": ['Taco']}

SEA = {'id': 'f1ae552b032c2d87a416f4067eaf4636b3fe5e80230a1f63aa33f6bc',
 'pool': 'SEA',
 'traits': 
['Holographic',
 'Red Tiger',
 'Hoskytwo',
 'Unknown',
 'Ghosky',
 'Cardoggo',
 'Vasil Mask',
 'War Paint',
 'Navy',
 'Green Gradient',
 'Extra Stank',
 'Ganja',
 'Blue Purple Gradient',
 'Jes Art',
 'Double Bandaged Ears',
 'Snorkel',
 'Silver Crown',
 'Reindeer',
 'Hosk Cap',
 'Halo',
 'Neon Sphinx Hat',
 'Trent Barnes',
 'Cone',
 'Dizzy Eyes',
 'Hypno Dizzy Eyes',
 'Brown Eyes',
 'Rolls Eyes',
 'Stoned Eyes',
 'Test Card',
 'Flies',
 'Flies Animated',
 'Knitted Mouth',
 'Red Laser',
 'EyePatch Left',
 'EyePatch Right',
 'Tears'],"gnome_traits": ['Yacht','Playboy']}

WOOF = {'id': 'c22942e1b855136643d1e6e5a75266fb891d87727a8cbf06acd17208',
 'pool': 'WOOF',
 'traits': 
['Joker',
 'Original Retired',
 'Green',
 'Snowfall',
 'Beige',
 'Light Blue Gradient',
 'Hosky Blue Gradient',
 'FIN',
 'Double Right Rings',
 'Bone',
 'Sweatband',
 'Blood Poo',
 'Sweatband 2',
 'Cork Hat',
 'Sphinx Hat',
 'FUD Cap',
 'Paper Bag',
 'Hawaiian',
 'Black Bowtie',
 'Blue Eyes',
 'Cyclops Eyes',
 'White Glowing Eyes',
 'Clown Eyes',
 'Left or Right Eyes',
 'Scarred Eyes',
 'Pernis Vs Wernis',
 'Golden Shine',
 'Thug Life',
 'Upside Down Right Way Up'],"gnome_traits": ['Idiot']}

HERO = {'id': '259d8027c33ee454ec2319531269495c07fefcdb52a513c5090f59ed',
 'pool': 'HERO',
 'traits': 
['Blue Dog',
 'Skull',
 'NSFW',
 'Grey',
 'Deep Green',
 'Dimalix',
 'White Earphones',
 'Goatee',
 'Hero',
 'Red Wooly Hat',
 'Blue Wooly Hat',
 'Hero 2',
 'Cowboy Hero',
 'Red Collar Gold Spikes',
 'Bow tie',
 'Wood',
 'Balloon',
 'Jigsaw',
 'LED Mouth',
 'Dollar Mouth',
 'Stitched Up',
 'Visor Meh',
 'Stitches',
 'Hero Mask'],"gnome_traits": ['Pernis','NFT Guru']}

FARM = {'id': '6879ab43e837d11c606e37dbf3e743f13f303c9dff53be602f263d6d',
 'pool': 'FARM',
 'traits': 
['Gold',
 'Ginger',
 'Khaki',
 'Fireplace',
 'Red Gradient',
 'Iris',
 'Green Purple Gradient',
 'Granite',
 'Cosmos',
 'Candle Right',
 'Flaming Hot',
 'Robin Hood',
 'Martian',
 'Karen',
 'Buffon Hat',
 'Prisoner 42069',
 'Afro',
 'Rainbow Hat',
 'Lawyer Wig',
 'Blue Collar Gold Spikes',
 'Black Eye',
 'Poo',
 'Food',
 'Zero',
 'Snowman',
 'Sausage',
 'Duckface',
 'Uncertain',
 'Blingin',
 'Visor Beam',
 'Pilot Glasses Tinted'],"gnome_traits": ['Hunter']}

PSYA = {'id': '111646b0848804b1c0ff51888432c9c4b0b0aa3b55f11ecbd0e36624',
 'pool': 'PSYA',
 'traits': 
['Yellow Dog',
 'Radioactive Orange',
 'Family',
 'Red',
 'Black Radioactive',
 'Carbon Fiber',
 'Radioactive Yellow',
 'Blue Yellow Gradient',
 'Diamond Stud',
 'Crumpet',
 'Spin Top',
 'Santa Hat',
 'McDonalds Manager',
 'Purple Hat',
 'Fighter Pilot',
 'Gold Bowtie',
 'Pink Eye',
 'Hypno Eyes',
 'Frosty',
 'Zeros Around the World',
 'Banksy Tribute',
 'Upside Down'],"gnome_traits": ['Cheshire']}

PSB = {'id': 'f2fa0dfea7f4caba8cbdd042c4940c783ee57f9516062725b04e19a3',
 'pool': 'PSB',
 'traits': 
['Hoskasaur',
 'Knitted',
 'Crazy Mary',
 'Prison',
 'Matrix',
 'Blue Stepped Gradient',
 'Stud Left',
 'Fighter Pilot Mask',
 'Red Lunar New Year Hat',
 'HoskyMando',
 'Red Wooly Hat Error',
 'Squid Game Triangle',
 'Reindeer Error',
 'Horns',
 'Blue Poncho',
 'Pink Eye',
 'Spicy Eyes',
 'Lunar new year wave',
 'Thinking',
 'Happy',
 '3D Gloss'],"gnome_traits": ['McHosky']}

SALT = {'id': 'ea90b56d9c4d04c583ec728c8b415948b310d4653d12bd281aaff9df',
 'pool': 'SALT',
 'traits': 
['Hosky Droid',
 'Original OAP',
 'Purple',
 'Orchid',
 'Double Left Rings',
 'Beard',
 'Top Hat Blue',
 'Tiger Hat',
 'Micky',
 'YOLO Hat',
 'Desert Camo',
 'Hosk Chain',
 'Crazy Eyes',
 'Vegas Eyes',
 'Coqui Eyes',
 'Candy Cane',
 'Out Of Ink',
 '3D Glasses',
 'Monocle'],"gnome_traits": ['Playboy','Yacht']}

A3C = {'id': '159bd971439653da2b97d12facae06ff5e6d7410d074edaab425202b',
 'pool': 'A3C',
 'traits': 
['Pink',
 'Coyote',
 'Coqui',
 'Late Night',
 'Happy Trees - JES Art',
 'Brickwall',
 'Consensus 2022 Uncommon',
 'Jackson Pollock',
 'Orange',
 'Stickers',
 'Neon',
 'Blue Grid',
 'Beauty Mark',
 'Big Moustache',
 'Crown',
 'Mardis Gras Hat',
 'Trash Can Lid',
 'Forest Camo',
 'TBLH Hat',
 'Blue Collar',
 'Vicar',
 'The Fools Neck',
 'Hoskytwo Eyes',
 'Damien Hirst',
 'Consensus 2022',
 'Dice',
 'Newspaper',
 'Fingerpaint',
 'Crypto Magazine',
 'Rob Boss Beard',
 'Visor Dead',
 'Fighter Pilot Glasses'],"gnome_traits": ['Classic']}

BONE = {'id': '97aaa4621cffb87c3e8380376406cc9501d6c9e1cbb459e17cd60602',
 'pool': 'BONE',
 'traits': 
['Baby Blue',
 'Scruff',
 'Poo',
 'This is Fine',
 'Ukraine',
 'Spamdle',
 'Busy',
 'Fluorescent Gradient',
 'Sunset Tones Gradient',
 'Livestream',
 'Obsidian',
 'Bandaged Ear Right',
 'Tongue Out',
 'Police',
 'Holographic Hat',
 'Blue Hat',
 'Beret',
 'Chef Hat',
 'Annie Hat',
 'Bloody Arrow',
 'Faux Rug Survivor',
 'Bloodyhell',
 'Check Mate',
 'Mega Pint',
 'FIRED!',
 'Hosky 2000 Computer',
 'Retro Coins',
 'Aboslutely',
 'Hmmm',
 'Cyber Hosky 2.0',
 'Sunset Glasses'],"gnome_traits": ['Taco']}

PRIDE = {'id': '93ca5c2f1eb63054f7c768a807408a43e65d7c68fe56e330db20af51',
 'pool': 'PRIDE',
 'traits': 
['Doberman',
 'LED',
 'Cyan',
 'Pop Art',
 'Candle Middle',
 'Rainbow Vomit',
 'Black lunar new year hat',
 'Fez',
 'Dank Hat',
 'Neckerchief',
 'Overload',
 'Flaming Hot Eyes',
 'Cact-eyes',
 'Wernis',
 'Felt',
 'Sunlight',
 'Ooooo',
 'Back To The Future',
 'Broken Pilot Glasses'],"gnome_traits": ['Classic']}

NANI = {"id": "d0deba25ce9e6ff59af7f39305fce373241156616cdf0a49b1d49e48",
       "pool": "NANI",
       'traits':
        ['X-Ray',
 'Ghost',
 'Radioactive Green',
 'Grinch',
 'Fox',
 'Dark Black',
 'Sahara',
 'Red Earphones',
 'Tooth',
 'Poo Hat',
 'Red lunar new year hat',
 'We Need You',
 'Mohican',
 'Stay Palm',
 'Stay Palm Gold',
 'Doggy Bowl',
 'Overload',
 'Robot Eyes',
 'Glowing Eyes',
 'Twitchy Eyes',
 'Blinking',
 'Warning',
 'Spinning Bowtie',
 'WTF',
 'Snowman Error',
 'Yellow Laser',
 'Wipers'], "gnome_traits": ["HOCSI WEN"]}


#POOLS_BECH_32 = {"SEA": }


#BlOCKFROST PARAMS HEADERS

params = {"count": 100,"page": 1, "order": "desc"}
project_id = os.environ.get("PROJECT_ID")
headers={"project_id": project_id}


#SOME GLOBALS


#filename = "hosky_asset_names.json"
filename2 = "hosky_asset_metadata_cleaned.json"
#filename3 = "hosky_asset_names_update.json"

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     HELPERS        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def has_more_pages(response):
    if len(response)==100:
        return True
    
def strip_policy(asset):
    if asset.startswith(POLICY_ID):
        return asset.replace(POLICY_ID,"")
    if asset.startswith(POLICY_ID_2):
        return asset.replace(POLICY_ID_2,"")


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     SEQUENCE BASE        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     SAFE        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Define the relative path to the src folder

script_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(script_path)

def sync_update(cashg_up, gnomes_up):
    with open(os.path.join(src_path, "hosky_asset_metadata_cleaned.json"), "r") as infile:
        data = json.load(infile)
        data[POLICY_ID].update(cashg_up)
        data[POLICY_ID_2].update(gnomes_up)
    temp = data
    return temp

def safe_update(data):
    # Define the relative path to the file within the src folder
    filename2_path = os.path.join(src_path, "hosky_asset_metadata_cleaned.json")

    os.remove(filename2_path)
    with open(filename2_path, "x") as f_name: 
        json.dump(data, f_name)
       
    return "success"

def overwrite_pool_stats_latest(data):
    file_path = os.path.join(src_path, 'pool_stats_latest.json')
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     ANALYZE WALLETS FOR NFTS HELPERS        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def get_delegators(pool_id):
    delegators = list(rq.get(f"https://pool.pm/stake/{pool_id}").json().keys())
    #pp.pprint(len(wallets))
    return delegators

def clean_list(some_list):
    cleaned_list = []
    #cleans all non hosky nfts from list
    
    for dictionary in some_list:
        values = dictionary.values()
        for value in values:
            if value.startswith(POLICY_ID):
                cleaned_list.append(value)
            elif value.startswith(POLICY_ID_2):
                cleaned_list.append(value)
            elif value.startswith(POLICY_ID_S):
                cleaned_list.append(value)
            elif value.startswith(POLICY_ID_SPECIAL):
                cleaned_list.append(value)
    return cleaned_list
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     ANALYZE WALLETS FOR NFTS        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def pool_assets(pool_id):
    pool_id = pool_id
    asset_list = []
    cgs_with_shittis = 0
    cgs_with_shittis_count = 0
    addresses = get_delegators(pool_id)
    
    url = "https://api.koios.rest/api/v0/account_assets"
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    
    # Enable requests caching
    requests_cache.install_cache("api_cache", expire_after=3600)  # Cache expires after 1 hour
    
    retry_attempts = 0
    retry_delay = 60
    
    # Stream addresses in batches of 250
    for i in range(0, len(addresses), 250):
        batch_addresses = addresses[i:i+250]
        
        data = {
            "_stake_addresses": batch_addresses
        }
        
        while retry_attempts < 5:  # Maximum number of retry attempts
            try:
                response = rq.post(url, headers=headers, json=data, timeout=60)
            
                if response.status_code == 200:
                    print("POST request was successful!")
                    output = response.json()
                    break
                
                print(f"Request failed with status code {response.status_code}. Retrying in {retry_delay} seconds...")
                t.sleep(retry_delay)
                
                retry_attempts += 1
                retry_delay += 60  # Increment retry delay by 60 seconds
            
            except rq.exceptions.RequestException as e:
                # Handle connection errors or other exceptions
                print(f"Request failed with exception: {e}")
                print(f"Retrying in {retry_delay} seconds...")
                t.sleep(retry_delay)
                
                retry_attempts += 1
                retry_delay += 60  # Increment retry delay by 60 seconds
        
        else:
            print("Maximum retry attempts reached. Exiting...")
            return {"pool nfts": asset_list, "cgs with shittis": cgs_with_shittis}
        
        for i in output:
            assets = [asset["policy_id"] + asset["asset_name"] for asset in i["asset_list"] if asset["policy_id"] in [POLICY_ID, POLICY_ID_2, POLICY_ID_S, POLICY_ID_SPECIAL]]
            asset_list.extend(assets)
            shitti_detection = [asset for asset in assets if asset.startswith(POLICY_ID_S)]
            
            if shitti_detection:
                cgs_with_shittis_count = len([cash_grab for cash_grab in assets if cash_grab.startswith(POLICY_ID)])
                cgs_with_shittis += cgs_with_shittis_count
                print(f"We have {cgs_with_shittis} CGs with shittis")
                cgs_with_shittis_count = 0
    
        t.sleep(30)  # Sleep for 30 seconds after each batch
    
    return {"pool nfts": asset_list, "cgs with shittis": cgs_with_shittis}

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      HELPERS        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

script_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(script_path)
src_path = os.path.join(parent_path, 'src')

def open_metadata():
    file_path = os.path.join(src_path, 'hosky_asset_metadata_cleaned.json')
    with open(file_path, "r") as f:
        data = json.load(f)
        Metadata = data[POLICY_ID] 
    return Metadata

def open_metadata_2():
    file_path = os.path.join(src_path, 'hosky_asset_metadata_cleaned.json')
    with open(file_path, "r") as f:
        data = json.load(f)
        Metadata_2 = data[POLICY_ID_2]
    return Metadata_2

def is_matched(Metadata,Pool_Traits):
    for trait in Metadata:
        if trait in Pool_Traits:
            return True


def asset_in_data(asset,metadata):
    if asset in metadata:
        return metadata[asset]

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      SYNC         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def sync_metadata(asset_name):
    t.sleep(0.16)
    
    if asset_name.startswith(POLICY_ID) == True:
        policy = POLICY_ID
    if asset_name.startswith(POLICY_ID_2) == True:
        policy = POLICY_ID_2
        
    asset_name = strip_policy(asset_name)
    traits = {asset_name : []}
    #print("#S#",asset_name,"/",policy,"#S#")
    
    try : 
        r = rq.get(f"https://api.koios.rest/api/v0/asset_info?_asset_policy={policy}&_asset_name={asset_name}",timeout = 30)
        status = r.status_code
        if status == 200:
            try:
                r_json = r.json()
                asset_name_ascii = r_json[0] ["asset_name_ascii"]
                traits_path = r_json[0] ["minting_tx_metadata"] ["721"] [policy] [asset_name_ascii] ["-----Traits-----"]
                for dictionary in traits_path:
                    values = list(dictionary.values())
                    for value in values:
                        traits[asset_name].append(value)
                return traits
            except Exception as e:
                print(e)
                return None
    except Exception as e:
        print(e)
        pass
   
    try:
        asset = policy+asset_name
        r = rq.get(f"https://cardano-mainnet.blockfrost.io/api/v0/assets/{asset}",params=params,headers=headers, timeout = 30)
        r_json = r.json()
        traits_path = r_json ["onchain_metadata"] ["-----Traits-----"]
    except Exception as e: 
        print(e)
        return None
    
    for dictionary in traits_path:
        values = list(dictionary.values())
        for value in values:
            traits[asset_name].append(value)
    return traits



def sync_all(asset_names_list):
    mf = []
    gnomes_up = {}
    cashg_up = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(sync_metadata, asset_names_list)
        for result in results:
            if result == None:
                print("None")
            else:
                mf.append(result)    
    for dictionary in mf:
        for key, value in dictionary.items():
            if key.startswith("476"):
                gnomes_up.update(dictionary)
            elif key.startswith("484"):
                cashg_up.update(dictionary)
            else: pass
    #print(len(mf))
    safe_update(sync_update(cashg_up,gnomes_up))
    mf_cleaned = {}
    for dictionary in mf:
        mf_cleaned.update(dictionary)
    return mf_cleaned
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def pool_stats(pool_dict):
    cashg = 0
    matched = 0
    shitti = 0
    gnome_special = 0
    gnome = 0
    matched_2 = 0
    sync_list = []
    
    
    pool_nfts_f = pool_assets(pool_dict["id"])
    cgs_with_shittis = pool_nfts_f["cgs with shittis"]
    pool_nfts = pool_nfts_f["pool nfts"]
    print("total: ", len(pool_nfts))
    
    Metadata = open_metadata()
    Metadata_2 = open_metadata_2()
    Pool_Name = pool_dict["pool"]
    Pool = pool_dict["traits"]
    Pool_2 = pool_dict["gnome_traits"]
    
    for asset in pool_nfts:
        asset_stripped = strip_policy(asset)
        
        if asset.startswith(POLICY_ID):
            cashg += 1
            in_data = asset_in_data(asset_stripped,Metadata)
            if in_data != None:
                if is_matched(in_data,Pool) == True:
                    matched += 1
                    
            else:
                sync_list.append(asset)
        elif asset.startswith(POLICY_ID_2):
            gnome += 1
            in_data = asset_in_data(asset_stripped,Metadata_2)
            if in_data != None:
                if is_matched(in_data,Pool_2) == True:
                    matched_2 += 1
                    
            else:
                sync_list.append(asset)
        elif asset.startswith(POLICY_ID_S):
            shitti += 1
        elif asset.startswith(POLICY_ID_SPECIAL):
            gnome_special += 1
        #print(f"cashgrabs matched:{matched}/{cashg}\ngnomes matched: {matched_2}/{gnome} \nshittis: {shitti}")
    print("to do : ",len(sync_list))
    if sync_list != {}:
        
        missing_traits = sync_all(sync_list)
        print("fetched: ",len(missing_traits))
        missing_traits_assets = list(missing_traits.keys())
        for asset in missing_traits_assets:
            if asset.startswith("484"):
                if is_matched(missing_traits[asset], Pool) == True:
                    matched += 1
            elif asset.startswith("476"):
                if is_matched(missing_traits[asset],Pool_2) == True:
                    matched_2 += 1
            
    weight = cashg + matched + ((gnome+matched_2)*15)+(cgs_with_shittis * 0.69) + (gnome_special * 5)
    matched_percentage = (matched / cashg)*100
    matched_percentage_2 = (matched_2 / gnome)*100
    
    #print(f"{Pool_Name};\nWeight: {weight} \ncashgrabs matched:{matched}/{cashg}\ngnomes matched: {matched_2}/{gnome} \ncgs with shittis: {cgs_with_shittis},and shittis: {shitti} \nspecial_gnomes: {gnome_special}")
    sequence = [{"pool": Pool_Name,"weight raw": weight, "cashg's": cashg,"cg matched": matched,"cg matched%": matched_percentage, "gnomeskies": gnome,"gn matched": matched_2, "gn matched%": matched_percentage_2, "special gnomes": gnome_special, "shittis with cgs": cgs_with_shittis,"shittis": shitti}]
    return sequence


pools = [RARE,SALT, CHEF, QCPOL, ITZA, SEA, WOOF, HERO, FARM, PSYA, PSB, A3C, BONE, PRIDE, VEGAS, HAZEL, FIKA, LIDO, NANI, STOIC] 



#asd = rq.get("https://cardano-mainnet.blockfrost.io/api/v0/metrics",headers=headers).json()
#asd

def plot_pools():
    catch = []
    for x in pools:
        start = t.perf_counter()
        catch.extend(pool_stats(x))
        finish = t.perf_counter()
        print("duration in s: ", start - finish)
    overwrite_pool_stats_latest(catch)
    print(catch)
    valor_ano = pd.DataFrame(catch).sort_values('weight raw', ascending=True)
    valor_ano.set_index("pool")

    plt.figure(figsize=(13, 10))

    sns.set_style("whitegrid")
    valor_plot = sns.barplot(
        data=valor_ano,
        x='pool',
        y='weight raw',
        errcolor="r",
        order=valor_ano.sort_values('weight raw', ascending=False).pool,
        palette="RdYlGn"
    )

    file_path = os.path.join(src_path, 'graph.png')
    plt.savefig(file_path, transparent=True, dpi=150)

plot_pools()
#print(get_delegators(SEA["id"]))

