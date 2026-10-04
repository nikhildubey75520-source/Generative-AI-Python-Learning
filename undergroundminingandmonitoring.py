class Mine:
    def __init__(self, name, location, gas, temperature, oxygen, workers):
        self.name = name
        self.location = location
        self.gas = gas
        self.temperature = temperature
        self.oxygen = oxygen
        self.workers = workers
    def safety_status(self):
        if self.gas > 50:
            return "DANGER - High Gas Level"
        elif self.temperature > 45:
            return "DANGER - High Temperature"
        elif self.oxygen < 19.5:
            return "DANGER - Low Oxygen"
        elif self.gas > 30 or self.temperature > 40:
            return "WARNING"
        else:
            return "SAFE"
class Emergency:
    def __init__(self, mine_id, emergency_type, severity):
        self.mine_id = mine_id
        self.emergency_type = emergency_type
        self.severity = severity
        self.rescue_status = "Rescue Team Not Assigned"
    def start_rescue(self):
        self.rescue_status = "Rescue Team Dispatched"
mines = dict()
emergencies = dict()
while True:
    print("\n UNDERGROUND MINE SAFETY SYSTEM")
    print("1. Add Mine")
    print("2. View Mine Safety Status")
    print("3. Search Mine")
    print("4. Update Safety Data")
    print("5. Report Emergency")
    print("6. View Active Emergencies")
    print("7. Start Rescue Operation")
    print("8. Delete Mine")
    print("9. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        mine_id = int(input("Enter Mine ID: "))
        name = input("Enter Mine Name: ")
        location = input("Enter Mine Location: ")
        gas = float(input("Enter Gas Level: "))
        temperature = float(input("Enter Temperature: "))
        oxygen = float(input("Enter Oxygen Level: "))
        workers = int(input("Enter Number of Workers: "))
        m = Mine(
            name,
            location,
            gas,
            temperature,
            oxygen,
            workers
        )
        mines[mine_id] = m
        print("Mine added successfully!")
        print("Safety Status:", m.safety_status())
    elif ch == 2:
        if len(mines) == 0:
            print("No mines available")
        else:
            print("\n MINE SAFETY STATUS ")

            for mine_id, m in mines.items():

                print("\nMine ID:", mine_id)
                print("Name:", m.name)
                print("Location:", m.location)
                print("Gas Level:", m.gas)
                print("Temperature:", m.temperature)
                print("Oxygen Level:", m.oxygen)
                print("Workers:", m.workers)
                print("Safety Status:", m.safety_status())
    elif ch == 3:
        mine_id = int(input("Enter Mine ID to search: "))
        if mine_id in mines:
            m = mines[mine_id]
            print("\n MINE DETAILS ")
            print("Mine ID:", mine_id)
            print("Name:", m.name)
            print("Location:", m.location)
            print("Gas Level:", m.gas)
            print("Temperature:", m.temperature)
            print("Oxygen Level:", m.oxygen)
            print("Workers:", m.workers)
            print("Safety Status:", m.safety_status())
        else:
            print("Mine not found")
    elif ch == 4:
        mine_id = int(input("Enter Mine ID to update: "))
        if mine_id in mines:
            m = mines[mine_id]
            m.gas = float(input("Enter new Gas Level: "))
            m.temperature = float(input("Enter new Temperature: "))
            m.oxygen = float(input("Enter new Oxygen Level: "))
            m.workers = int(input("Enter new Worker Count: "))
            print("Safety data updated successfully!")
            print("New Safety Status:", m.safety_status())
        else:
            print("Mine not found")
    elif ch == 5:
        emergency_id = int(input("Enter Emergency ID: "))
        mine_id = int(input("Enter Mine ID: "))
        if mine_id in mines:
            emergency_type = input(
                "Enter Emergency Type: "
            )
            severity = input(
                "Enter Severity (Low/Medium/High): "
            )
            e = Emergency(
                mine_id,
                emergency_type,
                severity
            )
            emergencies[emergency_id] = e
            print("Emergency reported successfully!")
        else:
            print("Mine not found")
    elif ch == 6:
        if len(emergencies) == 0:
            print("No active emergencies")
        else:
            print("\n ACTIVE EMERGENCIES")
            for emergency_id, e in emergencies.items():
                print("\nEmergency ID:", emergency_id)
                print("Mine ID:", e.mine_id)
                print("Emergency Type:", e.emergency_type)
                print("Severity:", e.severity)
                print("Rescue Status:", e.rescue_status)
    elif ch == 7:
        emergency_id = int(
            input("Enter Emergency ID: ")
        )
        if emergency_id in emergencies:
            e = emergencies[emergency_id]
            e.start_rescue()
            print("Rescue operation started!")
            print("Status:", e.rescue_status)
        else:
            print("Emergency not found")
    elif ch == 8:
        mine_id = int(input("Enter Mine ID to delete: "))
        if mine_id in mines:
            del mines[mine_id]
            print("Mine deleted successfully!")
        else:
            print("Mine not found")
    elif ch == 9:
        print("Underground Mine Safety System Closed!")
        break
    else:

        print("Invalid choice!")
