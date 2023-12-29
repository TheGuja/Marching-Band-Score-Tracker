from WGI_Groups import WGI
from LinkedList import LinkedList


if __name__ == '__main__':
    Ayala = WGI("Ayala HS", "World", 97.938, "4/22/23")
    Chino_Hills = WGI("Chino Hills HS", "World", 97.2, "4/22/23")
    Avon = WGI("Avon HS", "World", 96.738, "4/22/23")
    Vista_Murrieta = WGI("Vista Murrieta HS", "World", 96.113, "4/22/23")
    Center_Grove = WGI("Center Grove HS", "World", 95.05, "4/22/23")
    Dartmouth = WGI("Dartmouth HS", "World", 94.688, "4/22/23")
    Cy_Fair = WGI("Cy-Fair HS", "World", 93.413, "4/22/23")
    Broken_Arrow = WGI("Broken Arrow HS", "World", 90.788, "4/22/23")
    Clear_Brook = WGI("Clear Brook HS", "World", 90.575, "4/22/23")
    Burleson_Centennial = WGI("Burleson Centennial HS", "World", 90.313, "4/22/23")
    Arcadia = WGI("Arcadia HS", "World", 89.888, "4/22/23")
    Boswell = WGI("Boswell HS", "World", 89.2, "4/22/23")
    Sparkman = WGI("Sparkman HS", "World", 88.875, "4/22/23")
    Franklin_Central = WGI("Franklin Central HS", "World", 87.272, "4/22/23")
    Petal = WGI("Petal HS", "World", 86.475, "4/22/23")

    world_class = LinkedList()

    world_class_l = [Petal, Franklin_Central, Sparkman, Boswell, Arcadia, Burleson_Centennial, Clear_Brook, Broken_Arrow, Cy_Fair, Dartmouth, Center_Grove, Vista_Murrieta, Avon, Chino_Hills, Ayala]
    for group in world_class_l:
        world_class.add(group)

    world_class = world_class.mergeSort()
    input_response = ""

    while input_response.lower() != "q":
        input_response = input("\nEnter option from list below:\n1) Display Rankings\n2) Search for school\nQ) Quit\nResponse: ")

        if input_response == "1":
            print(world_class)
        elif input_response == "2":
            input_school = input("What school would you like to search for? ")
            if world_class.search(input_school) == None:
                print("School not found")
            else:
                print(world_class.search(input_school))
