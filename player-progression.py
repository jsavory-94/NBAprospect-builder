import random

#1.---CREATE PLAYER---

#   1.1 --Create Player Class--
class Player:
    def __init__ (self, name, age, position, traits, height, weight, wingspan, 
    bball_skill_inside, bball_skill_outside, bball_skill_control, bball_skill_IQ, bball_skill_athleticism):
        #Bio
        self.name = name
        self.age = age
        self.position = position
        self.traits = traits

        #Physical
        self.height = height
        self.weight = weight 
        self.wingspan = wingspan

        #Skillz
        self.bball_skill_inside = bball_skill_inside
        self.bball_skill_outside = bball_skill_outside
        self.bball_skill_control = bball_skill_control
        self.bball_skill_IQ = bball_skill_IQ
        self.bball_skill_athleticism = bball_skill_athleticism


    def player_ager(self):
        self.age +=1
    
    
    def teen_grower(self):
        growth_end_age = 20
        
        #define growth rates
        potential_mental_growthRate = 0.33 * (self.traits['game instinct']*0.01)
        actual_mental_growthRate = potential_mental_growthRate * random.uniform((self.traits['mental discipline']*0.01),1)
        
        potential_physical_growthRate = 0.09 * (self.traits['physical hardiness']*0.01)
        actual_physical_growthRate = potential_physical_growthRate * random.uniform((self.traits['training discipline']*0.01),1)

        #apply growth
        if self.age <= growth_end_age:
            self.bball_skill_IQ['offensive awareness'] += (99 - self.bball_skill_IQ['offensive awareness'])* (actual_mental_growthRate)
            self.bball_skill_IQ['defensive awareness'] += (99 - self.bball_skill_IQ['defensive awareness']) * (actual_mental_growthRate)
            self.bball_skill_athleticism['strength'] += (99 - self.bball_skill_athleticism['strength']) * (actual_physical_growthRate)
            
            if self.position == 'PF' or 'C':
                self.bball_skill_IQ['screen setting'] += (99 - self.bball_skill_IQ['screen setting']) * (actual_mental_growthRate)
            elif self.position == 'PG' or 'SG':
                self.bball_skill_IQ['screen using'] += (99 - self.bball_skill_IQ['screen using']) * (actual_mental_growthRate)               
            else:
                False            
        else:
            False

    #def early20s_grower(self):
    #   growth_end_age = 25
#
    #   #define growth rates
    #   potential_mental_growthRate = 0.33 * (self.traits['game instinct']*0.01)
    #   actual_mental_growthRate = potential_mental_growthRate * (self.traits['mental discipline']*0.01)



#   1.2 --Create Instances of Player--

#   1.2.1 --Define attributes--
def trait_inputter(bruce_lee, mental_disc, phys_hard, train_disc):
    return {'game instinct': bruce_lee, 'mental discipline': mental_disc, 'physical hardiness': phys_hard, 'training discipline': train_disc}

def skill_inside_inputter(stlayup, hook, dunk, shot_close, blk, offreb, defreb):
    return {'standing layup': stlayup, 'hook shot': hook, 'dunk': dunk, 'shot blocking': blk, 'offensive rebound': offreb, 'defensive rebound': defreb}

def skill_outside_inputter(mid, three, fade, stl):
    return {'shot mid': mid, 'shot three': three, 'post fade': fade, 'steal': stl}

def skill_control_inputter(handles, dish, dext, comp, post_off, post_def, peri_def):
    return {'ball handling': handles, 'passing': dish, 'dexterity': dext, 'composure':comp, 'post offense': post_off, 'perimeter defense': peri_def }

def skill_IQ_inputter(screen_set, screen_use, off_aware, def_aware):
    return {'screen setting': screen_set, 'screen using': screen_use, 'offensive awareness': off_aware, 'defensive awareness': def_aware}

def skill_athleticism_inputter(speed, strength, accel, jump, stamina):
    return {'speed': speed, 'strength': strength, 'acceleration': accel, 'jumping':jump, 'stamina':stamina}


#   1.2.2 --Create players--
player1 = Player('Dwayne "The Low Block" Johnson', 18, 'PF', trait_inputter(95,90,95,99), 76, 260, 77, 
                skill_inside_inputter(82, 67, 50, 70, 65, 90, 88), skill_outside_inputter(66,60,55,70), 
                skill_control_inputter(50,70,75,60,55,80,70), skill_IQ_inputter(66, 25, 70, 85), 
                skill_athleticism_inputter(60,95,65,65,88))

#print(player1.bball_skill_athleticism)



#2.---SIMULATE SEASONS---

print(f'On draft day {player1.name} is {player1.age} years old, and his skill of offensive awareness is ' + str(int((player1.bball_skill_IQ['offensive awareness']))))

season = 0
printcounter = 0

while season <=10:
    
    if printcounter == 1:
        print(f'After season {season}, {player1.name} is {player1.age} years old, and his skill of offensive awareness is ' + str(int((player1.bball_skill_IQ['offensive awareness']))))
        printcounter = 0

    player1.player_ager()
    player1.teen_grower()
        
    printcounter+=1
    season+=1

