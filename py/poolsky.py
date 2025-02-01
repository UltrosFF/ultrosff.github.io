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
#import blockfrost
#POLICIES

POLICY_ID="a5bb0e5bb275a573d744a021f9b3bff73595468e002755b447e01559"
POLICY_ID_2="ec77283fe87b1ccd7e5e8eb963de4c90abc8488e1e090b16b7f70a50"
POLICY_ID_S="de8086819da489257867042d568d4d7d4822387f94a092a578c40473"
POLICY_ID_SPECIAL= "dfdfc6dc2104fb78a54d942253439d86d550947307074eaa7e0de50c"





#POOLS_ID_AND_TRAITS

EASY1 = {
    'id': "20df8645abddf09403ba2656cda7da2cd163973a5e439c6e43dcbea9",
    "pool": "EASY1",
    "traits": [
        'bear', 'holographic', 'hoskpig', 'elementalfire', 
        'yellow', 'radioactiveyellow', 'epilogue', 'livestream', 
        'spiderlegs', 
        'redwoolyhat', 'bicyclehelmetred', 'blackandwhitejester', 
        'staypalmgold', 'silvercrownerror', 'bycocket', 'fastfood', 
        '2stplacemedal', 
        'seasick', 'hoskytwoeyes', 'sphinxeyes', 'elementalred', 
        'festiveholidaydogeyes', 
        'candycane', 'foolsgold', 'ngmi', 'trick', 
        'fliesanimated', 'enchantedfog'
    ],
    "gnome_traits": ["wedontexisthaha"]
}

MALU = {
    'id': "38927599cc3ff6b081501e0ee1dc4f0cb8ba012b3de8b49a785bb05a",
    "pool": "MALU",
    "traits": [
        'turtle', 'gravestone', 'sprinkles', 'radioactivepurple', 
        'goldframeception', 'ganja', 'slate', 'happytrees-jesart', 
        'orangepinkgradient', 'twilighttones', 
        'pizza', 
        'partyhat', 'yellowfeatherhat', 'chefhat', 'corkhat', 
        'horns', 'holographichat', 'headwrap', 'tophatrederror', 
        'superhero', 
        'wereeyes', 'blinking', 
        '1rdbirthdaypin', 'birthdayballoons', 
        'goodboy', 'happy', 'ooooo'
    ],
    "gnome_traits": ["wedontexisthaha"]
}


RARE = {'id': "dc31fffacd510b8a6accf2eecf59852ba4c18fcae383be5c37efd721",
        "pool": "RARE",
        "traits": ['Red Collar Gold Spikes', 'Doggy Bowl', 'Out-Of-Ink', 'Cyan', 'Poo', 'Granite', 'GN', 'Notepad', 'Sahara', 'Lunar New Year Red Animated', 'Playing Card', 'Vegas Computer', 'Prison Bars Animated', 'Miner', 'Santa Hat', 'Tea Cup', 'Theme Park', 'YOLO Hat', 'Blue Wooly Hat Error', 'Mollusk Print Play Error', 'Hoskasaur Eyes', 'Hypno Dizzy Eyes', 'Clown Eyes', 'Envy Eyes', 'Candle Left', 'Diamond Stud', 'Blue Dog', 'Tears', 'Retro Rainbow Eyes', 'Red Laser Error', 'Stitched Up', 'Original Mouth']
        , "gnome_traits": ["wedontexisthaha"]}

STOIC = {'id': "099d512b6ffedd552ae38a9ae2123c116b1d20e1f01bb42a1f539fba",
        "pool": "STOIC",
        "traits": ['Overload', 'Knackered', 'Coqui Eyes', 'Hosky Island Eyes', 'Banksy Tribute 4 of 4 by Danksy', 'Pernis', 'Space', 'Jes Art', 'Hosky Code', 'Film Noir', 'Orange Hazmat Suit', '<3', 'Jigsaw', 'Felt', 'Think S#!tty', 'Decentralised', 'Radioactive Pink', 'Hosky Sticker', 'Cardano Whale', 'Gold Tiger', 'Nose Glasses', 'Pilot Glasses Classic', 'Yellow Laser', 'Faux Rug Survivor', 'Pumpkin 2', 'Hero Error', 'Antlers'], "gnome_traits": ["not heard of yet"]}

HAZEL = {'id': 'be80794a946cf5e578846fc81e3c62ac13f4ab3335e0f5dc046edad4',
 'pool': 'HAZEL',
 'traits': ['Blue Collar Gold Spikes', 'Cigar', 'Flaming Hot', 'Spotty', 'Pernis Vs Wernis', 'Test Card', 'Aboslutely', 'Birthday Pin', 'Balloon', 'NSFW', 'Coqui', 'Werewolf', 'Catfish', 'Dark Spectre', 'Ghosky', 'Three Quarters There Original', 'Consensus 2022 Common', 'Green Yellow Gradient', 'Muddy Prints', 'Green Purple Gradient', 'Ukraine', 'Halloween', 'Twisted Clouds', 'Consensus 2022 Rare', 'Visor Meh', 'Cyber Hosky 2.0', 'Forest Camo', 'Splitting Headache', 'Bicycle Helmet Orange', 'Police Error', 'Crown Error', 'Mollusk Bone Play Error', 'Snowman Error'],"gnome_traits": ['McHosky']}

LIDO = {'id': 'b5a1a820cc3783a4e637bce79d1cc2774b241c08251e45c5d1f8f3f6',
 'pool': 'LIDO',
 'traits': ['WTF', 'Sad', 'Uncertain', "Blingin'", 'Banksy Tribute 3 of 4 by Danksy', 'Red', 'Sunset Tones Gradient', 'Vegas', 'Sunrise', 'Blue Grid', 'Top Hat Red', 'Headache', 'Blood Poo', 'Fez', 'Mohican', 'Viking Error', 'Red Wooly Hat Error', 'White Eyes', 'Coyote Eyes', 'Ukraine Eyes', 'Popped Eye', 'Rainbow Vomit', 'Neistat', 'Blue Laser Error', 'White Earphones', 'Zero', 'Another Holiday', '1st Anniversary', 'Light Spectre', 'Grey Alien', 'Red Tiger', 'Poo Bowtie'],"gnome_traits": ['Poolception','Lobster']}

BAIDU = {'id': 'c1f5cfd4330339e90ba83a64d269a81cf415d7adab36403e27b910f7',
 'pool': 'BAIDU',
 'traits': ['Yeh But No', 'Birthday Hat', 'Black Lunar New Year Hat', 'Top Hat Blue', 'Mardis Gras Hat', 'Hero 2', 'Blue Wooly Hat', 'We Need You', 'Sphinx Hat', 'Trash Can Lid', 'Double Stud Left', 'Beauty Mark', 'Birthday Cake', 'Dice', 'Charles Mask', 'Food Face', 'Family', 'Concrete Wall', 'Fireplace', 'Extra Stank', 'Stickers', 'Underwater Animated', 'Twilight Haunted Moon', 'Blue Poncho', 'Green Laser', '3D Gloss Error'],"gnome_traits": ['Rug Merchant']}

CHEF = {'id': '682fd73eea4d7370b6f7a781c80b1252817b23f74688cea6257471f3',
 'pool': 'CHEF',
 'traits': ['Oscar', 'Mummy', 'Green Alien', 'Banksy Tribute 2 of 4 by Danksy', 'Elemental Water', 'Green', 'April Fools', 'Lunar New Year Red', 'Carbon Fiber', 'Boo', 'Orange', 'Starry Night', 'Escher', 'Salvador Hosky', 'Double Stud Right', 'Engraved Skull', 'Visor', 'Visor Beam', 'Rob Boss', 'Light Blue Hat', 'Gold Ribbon Hat Error', 'Dune', 'Football Helmet', 'Santa Hat Error', 'Fast Food Error', 'Food Eyes', 'Left or Right Eyes', 'Elemental Blue', 'Elemental Gray', 'Knitted Mouth', 'Danksy Mouth', 'Retro Coins', 'Treat', 'Spinning Bowtie', 'S#!tty Cake', 'Blood', '1rd Place Medal'],"gnome_traits": ["Idiot"]}

VEGAS = {'id': '6a4a39566f5c45f0f6de34ef5e674b892e517ddeebd4eafcfd8583ef',
 'pool': 'VEGAS',
 'traits': ['Silver', 'Glass Jarsky', 'Rug Me Daddy!', 'Neon Blue', 'Dripping Blood', 'Navy', 'Peach', 'Late Night', 'Lunar New Year Blue', 'Black Radioactive', 'Obsidian', 'Light Blue Gradient', 'Pink', 'Raccoon', 'Fox', 'Crazy Mary', 'Purple Alien', 'Cardoggo', 'Ghost Eyes', 'Flaming Hot Eyes', 'Lightning Eyes', 'Hero Mask', 'Duckface', 'Sausage', 'Handlebar Moustache', 'HBI Hat', 'TBLH Hat', 'Silver Helmet'],"gnome_traits": ['Vegas','English']}

QCPOL = {'id': 'c2b8bff5160dd75149f2cae0955698550e8cf0d390025b26a9508a3e',
 'pool': 'QCPOL',
 'traits': ['Cigarette', 'Bubblegum', 'Strawberry', 'Fighter Pilot Mask', 'Eyepatch Left', 'Night Vision Goggles', 'Black Lennons', 'Flat Peak', 'Halo', 'Gold Ribbon Hat', 'Purple Hat', 'Lawyer Wig', 'Sweatband Error', 'Prison', 'Neon', 'Crimson Haunted Moon', 'Wind Gray Gradient', 'Vote', 'LED', 'Cut the Cake', 'Catastrophe', "It's Raining!", 'Black Bowtie', 'Diamond Chain', 'Bubblebath', 'Jake', 'Red Panda', 'Ape S#!t', 'Double Right Ring Errors'],"gnome_traits": ['Cheshire']}

ITZA = {'id': 'c29dd3c55a4f3f3b02aae6463ef8e1e66a70b5d000f8a6dc3430ef04',
 'pool': 'ITZA',
 'traits': ['Pink Eye', 'Heterochromia', 'Halfway Original', 'Mirrored Glasses', 'Goggles', 'Sunset Glasses', '3D Glasses Error', 'Spin Top', 'Crown', 'FUD Cap', 'Major Hosky', 'Poo Cap', 'Straw Hat', 'Poo Hat Error', 'Double Right Rings', 'Bandaged Ear Right', 'Red Earphones', 'Green Gradient', 'Blue Gradient', 'Cosmos', 'Dimalix', 'Maffs', 'Neon Pink Gradient', 'Beach', 'Green Haunted Moon', 'Zipped', 'War Paint', 'Yellow Dog', 'Radioactive Green', 'Hoskytwo', 'Jake Droopy', 'Out Of Ink', 'Crypto Ticker', 'Black and White Jester Neck'],"gnome_traits": ['Taco']}

SEA = {'id': 'f1ae552b032c2d87a416f4067eaf4636b3fe5e80230a1f63aa33f6bc',
 'pool': 'SEA',
 'traits': ['Grey', 'Deep Purple', 'Paint Splats', 'Morning Gradient', 'Old Computer', 'Community Birthday Card', 'Urban Wall Art', 'Fireplace Animated', 'Blood Orange Haunted Moon', 'Fire Red Gradient', 'Coyote', 'Mistakes Were Made', 'Robot 2.0 Rusty', 'Festive Holiday Dog', 'Cerberosky', 'Red Collar', 'Medicine Barrel', 'Cone', 'Dude', 'Snorkel', 'Snarl', 'Dollar Mouth', 'Flaming Hot Mouth', 'Barking', 'Gold Helmet', 'Mollusk Bowl Play', 'Brains'],"gnome_traits": ['Yacht','Playboy']}

WOOF = {'id': 'c22942e1b855136643d1e6e5a75266fb891d87727a8cbf06acd17208',
 'pool': 'WOOF',
 'traits': ['Whatsthat', 'Dizzy Eyes', 'Blue Eyes', 'Neon Sphinx Eyes', 'Hypno Eyes', 'Zombie Blood', 'Doberman', 'X-ray', 'Gold Skull', 'Looking The Other Way', 'Meh', 'Snowman', 'Traditional Painting', 'Lunar New Year Gold', 'Web', 'Ded', 'Golden Shine', 'Thug Life', 'Heads-Up Display', 'Fighter Pilot Glasses', 'Blue Laser', 'Spamsky Love', 'Neckerchief', 'SlumDogeEx-Millionaire', 'Solar Panels', 'Spamsky Studs', 'Reindeer', 'Mollusk Print Play', 'Fireworks', 'Blue Stepped Gradient', 'Snowfall Animated', 'Spamsky Sick'],"gnome_traits": ['Idiot']}

DDOS = {'id': 'a59e2c8422ed40242742f3b6e8219fa0c454eaa7288d71981d3b65a9',
 'pool': 'DDOS',
 'traits': ['White', 'Liberty', 'Scruff', 'Neon Sphinx', 'Chain', 'Stud Left', 'Double Left Rings', 'Newspaper', 'Hosky 2000 Computer', 'Zeros Around the World', 'Fog', 'Crumpet', 'Burgundy Moustache', 'Cowboy Hero', 'Afro', 'Stay Palm', 'Buffon Hat', 'Orange Hoodie', 'Clown Hair', 'Black Mask', 'Top Hat Blue Error', 'Trent Barnes', 'Brickwall', 'Duplicate', 'Race Track', 'Circles Animated', 'Upside Down Right Way Up', 'Asymmetrical Glasses', 'Stitches', 'Pilot Glasses Tinted', 'Red Eye Mask', 'Visor Dead', 'Eyepatch Right Error', 'Visor Animated', 'Cyclops Eyes'],"gnome_traits": ['Pernis','NFT Guru']}

FARM = {'id': '6879ab43e837d11c606e37dbf3e743f13f303c9dff53be602f263d6d',
 'pool': 'FARM',
 'traits': ['3D Gloss', 'Monocle', 'Bow Tie', 'Hawaiian', 'Wernis', 'Earth', 'Radioactive Yellow Animated', 'Dark Blue Haunted Moon', 'Consensus 2022', 'Wen', 'Poo Hat', "Aye Cap'n", 'Desert Camo', 'Hoskrogu Eyes', 'Brown Eyes', 'Hosky Droid', 'Golden', 'Radioactive Orange', 'Clown', 'Clay Face', 'Ascosky', 'Shaved', 'Gherkin Mouth', 'Sick'],"gnome_traits": ['Hunter']}

PSYA = {'id': '111646b0848804b1c0ff51888432c9c4b0b0aa3b55f11ecbd0e36624',
 'pool': 'PSYA',
 'traits': ['Crazy Eyes', 'Stoned Eyes', 'Cact-eyes', 'White Glowing Eyes', 'Rolls Eyes', 'Eyepatch Right', 'Lennon', 'Blue Eye Mask', 'Eat Poo', 'Left Ring', 'Hoskasaur', 'Ginger', 'Original Droopy Ear', 'Frankenhosk', 'Original Retired', 'Vegas Mask', 'Bycocket Error', 'Hero', 'Blue Hat', 'Space Invader', "Tea Cup World's Best Coder", 'Gold Poo Hat', 'King Tutankhamun', 'Theme Park Error', 'Neck Bolts', 'This is Fine', 'Consensus 2022 Uncommon', 'Sunlight'],"gnome_traits": ['Cheshire']}

PSB = {'id': 'f2fa0dfea7f4caba8cbdd042c4940c783ee57f9516062725b04e19a3',
 'pool': 'PSB',
 'traits': ['Ikea', 'Frosty', 'Thinking', 'Fairy Lights', 'Square Cake', 'Stamp', '1st Anniversary Fireworks', 'Please write something like happy 1st birthday hosky in blue', 'Sad-Ish', 'Rob Boss Beard', 'Clown Mouth', 'Third Ear Green', 'King Tutankhamun Error', 'Third Ear Orange', 'Mollusk Bone Play', 'Racing Helmet', 'Annie Hat', 'Third Ear Pink', 'Holographic Hat Error', 'Neon Sphinx Hat', 'Rainbow Hat', 'Khaki', 'Sunset Clouds Animated', 'Deep Green', 'Fuchsia', 'Pink Gradient', 'Spamdle', 'Radar Animated', 'Confetti Party', 'Moderator Birthday Card', 'Missing Bits', 'Tiger Fur', 'Knitted', 'Charles Eyes', 'Vasil Eyes', 'Glowing Eyes', 'Thug Life Error', 'Green Laser Error', 'Eyes Patched Error', 'Red Laser'],"gnome_traits": ['McHosky']}

SALT = {'id': 'ea90b56d9c4d04c583ec728c8b415948b310d4653d12bd281aaff9df',
 'pool': 'SALT',
 'traits': ['Bone', 'Tooth', 'Shizzle', 'Beard Error', 'Dark Black', 'Landscape', 'Hosky Island', 'Hexagon Green', 'Pop Art', 'Black Radioactive Animated', 'Banksy Tribute 1 of 4 by Danksy', 'Cyan Haunted Moon', 'Hoskrogu', 'Skull', 'Glow In The Dark Skull', 'Spicy Eyes', 'Psychedelic Eyes', 'Snowman Eyes', 'Sombrero', 'Prisoner 42069', 'Karen', 'Trucker', 'Red Lunar New Year Hat', 'Captain Error', 'Candle Right', 'Right Ring Error', 'Prison Bars', 'Shredder', 'FIRED!', '1rd Anonversary', 'Fingerpaint', 'Crypto Magazine Halloween Edition', 'Upside Down Error', 'Dude Error'],"gnome_traits": ['Playboy','Yacht']}

A3C = {'id': '159bd971439653da2b97d12facae06ff5e6d7410d074edaab425202b',
 'pool': 'A3C',
 'traits': ['Blue', 'Beige', 'Blue Purple Gradient', 'Neon Gradient', 'Orchid', 'Twilight Stepped Gradient', 'Highly Classified', 'Pastel', 'Confetti', 'Blue Yellow Gradient', 'Lunar New Year Blue Animated', 'Fireworks Animated', 'Bandana', 'Dumpling', 'Tiger Hat', 'Fast Food Manager Error', 'Green Hazmat Suit', 'Warning', 'Sticker', '!%*@#?', 'Torn', 'Shoot Out', '1rd Anonversary Fireworks', 'Señor Josquí', 'Hosk Chain', 'Blue Bowtie', 'LED Mouth', 'Twitchy Eyes', 'Eyes Patched', 'Biggie Hair', 'Candle Middle'],"gnome_traits": ['Classic']}

BONE = {'id': '97aaa4621cffb87c3e8380376406cc9501d6c9e1cbb459e17cd60602',
 'pool': 'BONE',
 'traits': ['Check Mate', 'Wood', 'Lunar New Year Wave', 'Wen Animated', 'Hmmm', 'Robot Mouth', 'Sunset', 'Red Gradient', 'Bright Blue Green Gradient', 'FIN', 'Pink Twilight Haunted Moon', 'Beard', 'Sphinx', 'Vasil Mask', 'Original OAP', 'Swampsky', 'Bloodyhell', 'Jake Eyes', 'Scarred Eyes', 'Hosk Cap', 'Spin Top Error', 'Reindeer Error', 'Robot Bowtie', 'Rug Pool Bowl', 'Orange Eye Mask', 'Wipers']
,"gnome_traits": ['Taco']}

PRIDE = {'id': '93ca5c2f1eb63054f7c768a807408a43e65d7c68fe56e330db20af51',
 'pool': 'PRIDE',
 'traits': ['Upside Down', 'Broken Pilot Glasses', 'Purple Eye Mask', 'Eyepatch Left Error', 'Purple', 'Fireworks Lunar New Year', 'Full Moon', 'Fluorescent Gradient', 'Rose', 'GM', 'Mint Gradient', 'Lightning', "It's Behind You", 'Deep Purple Haunted Moon', 'Earth Green Gradient', 'Beatenup', 'Robot Eyes', 'Danksy Eyes', 'Elemental Green', 'Right Ring', 'Pork Pie Hat', 'Elf Hat', 'Fast Food Manager', 'Arrow', 'The Fools Hat', 'Bloody Arrow', 'Elf Hat Error', 'Mega Pint', 'Food', 'Ghost Chain', 'Jaguar', 'Zombie', 'Elemental Earth', 'Elemental Wind', '1rd Chain'],"gnome_traits": ['Classic']}

ASPEN = {"id": "05b8a25ec4f41956a6496555c233bcbe6fc06596553ae2d14df73e20",
       "pool": "ASPEN",
       'traits': ['Blue Collar', 'Gold Bowtie', 'Sweatband', 'Green Hat', 'Idiot Hat', 'Paper Bag', 'Pumpkin', 'Stud Right', 'Bandaged Ear Left', 'Dizzy', 'Underwater', 'Clouds', 'Field Gradient', 'Snowfall', 'Peace', 'Salvador Hosky Animated', 'Grey Haunted Moon', 'Taco', 'Imagine Dragons', 'Ghost', 'Robot 2.0', 'Danksy', 'Fingerprint', 'Cyclops', 'Gherkin', 'Gold Glasses', 'Suits', 'Crypto Magazine Special Edition', 'Big Eyes'], "gnome_traits": ["HOCSI WEN"]}

GOMA = {"id": "9021035ba7bf0b5ecb49aba303fe9bd4b80d99f7b4519854f24f71a1",
       "pool": "GOMA",
       'traits': ['3D Glasses', 'Rainbow Visor', 'Yellow Laser Error', 'Police', 'Sweatband 2', 'Flat Peak Error', 'Beret', 'Fighter Pilot', 'Gladiator Mask', 'Black Eye', 'Ded Eyes', 'Cyan Glowing Eyes', 'Knitted Eyes', 'LED Eyes', 'HOSKY Turbo', 'Big Moustache', 'Tongue Out', 'Cocktail', 'Copper', 'Ghost Costume', 'Neon Green', 'Hosky Blocks', 'Flies', 'Double Bandaged Ears', 'Doodle', 'Robot', 'Static', 'Trash Can', 'Vicar', 'Violet Stepped Gradient', 'Press Start', 'Eighties', 'Light Speed', 'Fireworks Lunar New Year Animated', 'Fire Sky Haunted Moon', 'Water Blue Gradient'], "gnome_traits": ["HOCSI WEN"]}

HAWAK = {"id": "a24d65818d2aa00387f788e4d1da1cdaca138c50e9136af6cc55e68a",
       "pool": "HAWAK",
       'traits': ['Baby Blue', 'Mint', 'Glowing Pyramids', 'Iris', 'Bubbles', 'Busy', 'FIAT', 'Radar', 'Hosky Blue Gradient', 'After Party', 'Spamsky Gradient', 'Panda', 'Unknown', 'Spamsky', 'Goatee', 'Bubblegum Popped', 'Captain', 'Viking', 'Miner Error', 'Dank Hat', 'Bandana Error', 'Hero 2 Error', 'Mollusk Bowl Play Error', 'Mollusk S#1t Play', 'Mollusk S#1t Play Error', 'Spamsky Spamband', 'Love', 'Laser Visor', 'Late Night Glasses', 'Visor Heart', 'Love Error', 'Mirrored Glasses Error', 'Fish Bowl', 'Neon Pink', 'Astronaut', 'Crypto Magazine', 'Green Poncho', 'The Fools Neck', 'Spamsky Bling', 'Vegas Eyes', 'Three Eyes', 'Spamsky Original'], "gnome_traits": ["HOCSI WEN"]}


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
delegator_assets = []

def get_assets(delegator):
    assets_list = []
    filtered_2 = []
    assets = rq.get(f"https://cardano-mainnet.blockfrost.io/api/v0/accounts/{delegator}/addresses/assets",params=params,headers=headers, timeout = 30).json()
    filtered = clean_list(assets)
    assets_list.extend(filtered)
    filtered_2.extend(filtered)
    #print("total nfts of ^: ",len(assets))
    #print("delegator hosky nfts: ",len(filtered))
    cgs_with_shittis = 0
    shitti = False
    while True:
        
        if has_more_pages(assets) == True:
            #print("delegator has more: ",has_more_pages(assets))
            params["page"] += 1
            assets = rq.get(f"https://cardano-mainnet.blockfrost.io/api/v0/accounts/{delegator}/addresses/assets",params=params,headers=headers, timeout = 30).json()
            filtered = clean_list(assets)
            #print("on this page he had:", len(filtered))
            assets_list.extend(filtered)
            filtered_2.extend(filtered)
        
        else: 
            for asset in filtered_2:
                if asset.startswith(POLICY_ID_S):
                    shitti = True
                    break
            if shitti == True:
                for asset in filtered_2:
                    if asset.startswith(POLICY_ID):
                        
                        cgs_with_shittis += 1
            break
    #print("delegator had shitti: ",shitti,"add cg with shitti: ", cgs_with_shittis)
    params["page"] = 1
    return {"assets_list":assets_list,"cgs_with_shittis":cgs_with_shittis}

def pool_assets(pool_id):
    
    delegators = get_delegators(pool_id)
    #delegators = ["stake1uxmfu2tkg9wk0utmla8ns78udpy4d7dhc8gg5g3gt4a05tgfqm76y"]
    
    cgs_with_shittis = 0
    
    print("Total Delegators",len(delegators))
    pool_assets = []
    for delegator in delegators:
        #print("\ndelegator: "+delegator)
        assets_dict = get_assets(delegator)
        assets = assets_dict["assets_list"]
        cgs_with_shittis += assets_dict["cgs_with_shittis"]
        #print("cgs_with_shittis: ",cgs_with_shittis)        
        pool_assets.extend(assets)
        #print("new total is: ", len(pool_assets))
    return {"pool nfts":pool_assets,"cgs with shittis": cgs_with_shittis}

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


pools = [EASY1, MALU, GOMA, HAWAK, RARE, SALT, CHEF, QCPOL, ITZA, SEA, WOOF, DDOS, FARM, PSYA, PSB, A3C, BONE, PRIDE, VEGAS, HAZEL, BAIDU, LIDO, ASPEN, STOIC] 



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
