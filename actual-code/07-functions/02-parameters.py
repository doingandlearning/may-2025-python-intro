def describe_particle(name="Muon", mass=105.66):
    print(f"Particle: {name}")
    print(f"Mass: {mass} MeV/c^2")


describe_particle()

# do the work to look up the name and mass ...
describe_particle("Electron", 0.511)