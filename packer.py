import os
import json
import uuid
import time

def add_skins(name):
    os.system("CLS")
    print(f"Packaging [{name}]...\n")
    print("Type 'add [name]' to add a new skin.\nType 'remove [name]' to remove an existing skin.\nType 'list' to see your current skins.\nType 'done' when you are finished.\n")
    
    skin_list = []
    user_choice = ""
    while (True):
        user_choice = input(">>> ").strip()
        if (user_choice.startswith("add ")):
            skin_list.append(user_choice[4:])
            print(f"\nAdded new skin '{user_choice[4:]}'\n")
        elif (user_choice.startswith("remove ")):
            try:
                skin_list.remove(user_choice[7:])
                print(f"\nRemoved the skin '{user_choice[7:]}'\n")
            except ValueError:
                print("\nSkin does not exist!\n")
        elif (user_choice == "list"):
            if (skin_list):
                print("")
                for i in range(len(skin_list)):
                    print(f"Skin #{i + 1}: {skin_list[i]}")
                print("")
            else:
                print("\nNo skins added yet!\n")
        elif (user_choice == "done"):
            return skin_list
        else:
            print("\nUnrecognized input or arguments!\n")
    
def create_manifest_json(parent_directory, header_uuid, modules_uuid, version):
    manifest_json = {
        "header": {
            "name": "pack.name",
            "description": "pack.description",
            "version": version,
            "uuid": header_uuid
        },
        "modules": [
            {
                "version": version,
                "type": "skin_pack",
                "uuid": modules_uuid
            }
        ],
        "format_version": 1
    }
    with open(f"{parent_directory}Content/skin_pack/manifest.json", "x") as manifest_file:
        manifest_file.write(json.dumps(manifest_json, indent=2))
        
def create_skins_json(parent_directory, skins):
    skins_list = []
    for skin in skins:
        skins_list.append({
            "localization_name": skin,
            "geometry": "geometry.humanoid.customSlim",
            "texture": f"{skin}_customSlim.png",
            "type": "paid"
        })
    skins_json = {
        "skins": skins_list,
        "serialize_name": "Pop",
        "localization_name": "Pop"
    }
    with open(f"{parent_directory}Content/skin_pack/skins.json", "x") as skin_file:
        skin_file.write(json.dumps(skins_json, indent=2))

def create_en_us_lang(pack_name, parent_directory, skins):
    with open(f"{parent_directory}Content/skin_pack/texts/en_US.lang", "x") as us_lang_file:
        us_lang_file.write(f"skinpack.Pop={pack_name}")
        for skin in skins:
            us_lang_file.write(f"\nskinpack.Pop.{skin}={skin}")

def create_languages_json(parent_directory):
    languages_json = ["en_US"]
    with open(f"{parent_directory}Content/skin_pack/texts/languages.json", "x") as languages_file:
        languages_file.write(json.dumps(languages_json, indent=2))
        
def create_files(pack_name, skins):
    # Intialization
    parent_directory = f"./{pack_name.replace(' ', '_')}/"

    header_uuid = str(uuid.uuid4())
    modules_uuid = str(uuid.uuid4())
    version = [1, 0, 0]

    directories = [
        parent_directory,
        f"{parent_directory}Content/",
        f"{parent_directory}Content/skin_pack/",
        f"{parent_directory}Content/skin_pack/texts/",
        f"{parent_directory}Marketing Art/",
        f"{parent_directory}Store Art/",
    ]
    
    # Create all directories
    for dir in directories:
        os.mkdir(dir)
    
    # Create text files individually
    create_manifest_json(parent_directory, header_uuid, modules_uuid, version)
    create_skins_json(parent_directory, skins)
    create_en_us_lang(pack_name, parent_directory, skins)
    create_languages_json(parent_directory)
    
def create_skinpack():
    os.system("CLS")
    print("Initializing a new skinpack...\n")
    
    pack_name = input("Enter skin pack name: ").strip()
    skins = add_skins(pack_name)

    create_files(pack_name, skins)
    
    return pack_name

# Begin prompt
user_choice = ""
while (True):
    os.system("CLS")
    print("Packer™ for Monkey Slap Nut\n")
    print("Type 'new' to package a new skinpack.\nType 'quit' to exit.\n")
    user_choice = input(">>> ").strip()
    match user_choice:
        case "new":
            new_pack_name = create_skinpack()
            os.system("CLS")
            print(f"Successfully created [{new_pack_name}]!")
            time.sleep(2)
        case "quit":
            break
        case _:
            print("\nUnrecognized input, enter 'new' or 'quit'.\n")

