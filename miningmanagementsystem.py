class Mine:
    def __init__(self, name, location, mineral, production):
        self.name = name
        self.location = location
        self.mineral = mineral
        self.production = production
    def grade(self):
        if self.production >= 1000:
            return "High Production"
        elif self.production >= 500:
            return "Medium Production"
        elif self.production >= 100:
            return "Low Production"
        else:
            return "Very Low Production"
mining = dict()
while True:
    print("1. Add Mine")
    print("2. View Mines")
    print("3. Search Mine")
    print("4. Update Production")
    print("5. Delete Mine")
    print("6. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        mine_id = int(input("Enter Mine ID: "))
        name = input("Enter Mine Name: ")
        location = input("Enter Mine Location: ")
        mineral = input("Enter Mineral Type: ")
        production = int(input("Enter Production in Tons: "))
        m = Mine(name, location, mineral, production)
        mining[mine_id] = [
            m.name,
            m.location,
            m.mineral,
            m.production,
            m.grade()
        ]
        print("Mine added successfully!")
        print(mining)
    elif ch == 2:
        if len(mining) == 0:
            print("No mines available")
        else:
            print("\n ALL MINES")
            for mine_id, data in mining.items():
                print("Mine ID:", mine_id)
                print("Name:", data[0])
                print("Location:", data[1])
                print("Mineral:", data[2])
                print("Production:", data[3], "tons")
                print("Status:", data[4])
                print("")
    elif ch == 3:
        mine_id = int(input("Enter Mine ID to search: "))
        if mine_id in mining:
            print("\n MINE DETAILS")
            print("Mine ID:", mine_id)
            print("Name:", mining[mine_id][0])
            print("Location:", mining[mine_id][1])
            print("Mineral:", mining[mine_id][2])
            print("Production:", mining[mine_id][3], "tons")
            print("Status:", mining[mine_id][4])
        else:
            print("Mine not found")
    elif ch == 4:
        mine_id = int(input("Enter Mine ID to update: "))
        if mine_id in mining:
            production = int(
                input("Enter new production in tons: ")
            )
            m = Mine(
                mining[mine_id][0],
                mining[mine_id][1],
                mining[mine_id][2],
                production
            )
            mining[mine_id][3] = m.production
            mining[mine_id][4] = m.grade()
            print("Production updated successfully!")
        else:
            print("Mine not found")
    elif ch == 5:
        mine_id = int(input("Enter Mine ID to delete: "))
        if mine_id in mining:
            del mining[mine_id]
            print("Mine deleted successfully!")
        else:
            print("Mine not found")
    elif ch == 6:
        print("Mining Management System Closed!")
        break
    else:
     print("Invalid choice!")
