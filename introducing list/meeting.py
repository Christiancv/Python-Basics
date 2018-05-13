attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["james", "Guil"])
optional_invites = ["Ben j", "Dave"]
potential_attendees = attendees + optional_invites
print("There are", len(attendees), "potential attendees currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invites)
print("To: " + to_line)
print("CC: " + cc_line)