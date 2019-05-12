#!/usr/bin/python

from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This is the function executed when entering a new room. Subclass should override it."
        print "Unless the player has ended the game, this function should return a string of the next scene to enter"
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):

    orbituaries = [
            "The greatest programmer ever know has died today.",
            "Our Hero is dead. The Gothons Have One.",
            "GG Boi",
    ]


    def enter(self):
        print self.orbituaries[randint(0, len(self.orbituaries)-1)]
        exit(1)

class CentralCorridor(Scene):
    "This is the starting point and has a Gothon already standing there which the hero has to tell a joke before continuing"
    def enter(self):
        print "A Gothon Jumps out at you and is about to shoot. What do you do?['shoot', 'dodge', 'tell a joke']"
        while True:
            action = raw_input('> ')
            if action == "shoot":
                print "You are still too slow becuase you haven't had your coffee"
                return 'death'
            elif action == "dodge":
                print "You are too slow in this Gravity and yes, you haven't had your coffee"
                return 'death'
            elif action == "tell a joke":
                return 'laser_weapon_armory'

class LaserWeaponArmory(Scene):
    def enter(self):
        print "You find an armory but the laser weapons are kept in a safe with a 3 digit code"

        attempts = 0 
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "code = ", code
        while True:
            guess = raw_input('[keypad]> ')
            if guess == code:
                print 'Correct, Bruv. You nailed it using that cheat code >.<"!'
                return 'the_bridge'
            else:
                print "Incorrent!"
                attempts += 1
            if attempts == 3:
                print "Too Many attempts!"
                return 'death'
class TheBridge(Scene):
    def enter(self):
        print "On The Bridge are Gothons. What do you do with the bomb?[shoot, throw, place]"
        action = raw_input('> ')
        if action == "shoot":
            print "The bomb goes off"
            return 'death'
        elif action == "throw":
            print "You arm and throw the bomb and run but it goes off before you can return to your escape pod"
            return 'death'
        elif action == "place":
            print "You hold a gun to th ebomb while you slowly make for the escape pod"
            return 'escape_pod'
        else:
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print "Where the hero excapes but only after guessing the right escape pod."
        code = randint(1,9)
        attempt = 0
        print "The escape pod is protected by single digit code with 3 attempts."
        print "code =" , code
        while attempt < 3:
            guess = int(raw_input('> '))
            if code == guess:
                print "Our hero escapes to the planet below and the Gothan ship explodes."
                exit(0)
            else:
                print "Code Invalid! Try again."
                attempt +=1
        print "Too late, the bomb you placed on the bridge has detonated."
        return 'death'
class Finished(Scene):
    def enter(self):
        print "You won! Good Job!"
        return 'finished'

class Map(object):

    scenes = {
            'central_corridor' : CentralCorridor(),
            'laser_weapon_armory' : LaserWeaponArmory(),
            'the_bridge' : TheBridge(),
            'escape_pod' : EscapePod(),
            'death' : Death(),
            'finished' : Finished()
    }


    def __init__(self, start_scene):
         self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

