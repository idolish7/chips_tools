import test_data
import json
import gamelibrary_classes

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
    for game in game_library:
        #Create a new Game object from the json_data by reading
        #  title
        title = game["title"]
        #  year
        year = game["year"]
        new_game = gamelibrary_classes.Game(title, year)
        #  platform (which requires reading name and launch_year)
        platforms = game_library["platform"]
        for platform in platforms:
            new_platform = gamelibrary_classes.Platform(platform["launch_year"], platform["name"])
            new_game.add_platform(new_platform)
        #Add that Game object to the game_library
        game_library.append(game)
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
with open(input_json_file, "r") as reader:
    #Use the json module to load the data from the file
    gamelibrary_json_data = json.load(reader)

#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
new_gamelibrary = make_game_library_from_json(gamelibrary_json_data)
#Print out the resulting GameLibrary data using print()
print(new_gamelibrary)
### End Add Code Here ###
