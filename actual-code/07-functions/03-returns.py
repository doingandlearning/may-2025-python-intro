def energy(momentum, mass, units="MeV"):
    if units != "MeV" and units != "GeV":
        return "Invalid units"
    e = (momentum**2 + mass**2)**0.5
    if units == "GeV":
        e /= 1000
    return e


e = energy(300, 105.66)
print(f"{e} MeV")

e = energy(300, 105.66, "GeV")
print(f"{e} GeV")

e = energy(300, 105.66, "J")
print(f"{e} J")