import cc_dat_utils
import json
import cc_classes

#Part 3
#Load your custom JSON file
# Open and read level json
def load_read_json():
  input_json_file = "cc_custom_json.json"
  with open(input_json_file, "r") as reader:
    #Use the json module to load the data from the file
    levelpack_json_data = json.load(reader)
    return levelpack_json_data

#Convert JSON data to CCLevelPack
def make_level_pack_from_json(json_data):
  newLevelPack = cc_classes.CCLevelPack() # level or level pack?

  for level in json_data:
    ### New level
    newLevel = cc_classes.CCLevel()

    ### Level attributes
    newLevel.time = level["time"]
    newLevel.num_chips = level["chipNum"]
    newLevel.level_number = level["levelNum"]
    newLevel.upper_layer = level["upperLayer"]

    ### Optional fields
    title = cc_classes.CCMapTitleField(level["fields"][0]["title"])
    newLevel.add_field(title)

    # Password array
    passwordArr = []
    for passint in level["fields"][0]["password"]:
      passwordArr.append(passint)
    password = cc_classes.CCEncodedPasswordField(passwordArr)
    newLevel.add_field(password)

    hint = cc_classes.CCMapHintField(level["fields"][0]["hint"])
    newLevel.add_field(hint)

    monsterPath = []
    for pathtuple in level["fields"][0]["monster"]:
      coord = cc_classes.CCCoordinate(pathtuple[0], pathtuple[1])
      monsterPath.append(coord)
    monster = cc_classes.CCMonsterMovementField(monsterPath)
    newLevel.add_field(monster)
    newLevelPack.add_level(newLevel)

  # Add level to pack
  return newLevelPack
    
if __name__ == "__main__":
  # Load and read
  levelpack_json_data = load_read_json()
  # Create a level pack object from the json
  new_level_pack = make_level_pack_from_json(levelpack_json_data)
  #Save converted data to DAT file
  dat_level = "cc_assignment_dat.dat"
  cc_dat_utils.write_cc_level_pack_to_dat(new_level_pack, dat_level)
  
  print(cc_dat_utils.make_cc_level_pack_from_dat(dat_level))

# move "cc_assignment_dat.dat" that is generated in the root folder to the data folder of tworld
# run tworld and play your level!