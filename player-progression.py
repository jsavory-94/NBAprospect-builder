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
        potential_mental_growthRate = 0.33 * (self.traits['mental drive']*0.01)
        actual_mental_growthRate = potential_mental_growthRate * (self.traits['mental discipline']*0.01)
        
        potential_physical_growthRate = 0.09 * (self.traits['physical hardiness']*0.01)
        actual_physical_growthRate = potential_physical_growthRate * (self.traits['training discipline']*0.01)

        #apply growth
        if self.age < growth_end_age:
            self.bball_skill_IQ['offensive awareness'] = self.bball_skill_IQ['offensive awareness'] * (1 + actual_mental_growthRate)
            self.bball_skill_IQ['defensive awareness'] = self.bball_skill_IQ['defensive awareness'] * (1 + actual_mental_growthRate)
            if self.position == 'PF' or 'C':
                self.bball_skill_IQ['screen setting'] = self.bball_skill_IQ['screen setting'] * (1 + actual_mental_growthRate)
            elif self.position == 'PG' or 'SG':
                self.bball_skill_IQ['screen using'] = self.bball_skill_IQ['screen using'] * (1 + actual_mental_growthRate)
            else:
                False
            self.bball_skill_athleticism['strength'] = self.bball_skill_athleticism['strength'] * (1 + actual_physical_growthRate)

        else:
            False


#   1.2 --Create Individual Players--

#   1.2.1 --Define attributes--
def trait_inputter(mental_drive, mental_disc, phys_hard, train_disc):
    return {'mental drive': mental_drive, 'mental discipline': mental_disc, 'physical hardiness': phys_hard, 'training discipline': train_disc}

def skill_inside_inputter(stlayup, hook, dunk, shot_close, blk, offreb, defreb):
    return {'standing layup': stlayup, 'hook shot': hook, 'dunk': dunk, 'shot blocking': blk, 'offensive rebound': offreb, 'defensive rebound': defreb}

def skill_outside_inputter(mid, three, fade, stl):
    return {'shot mid': mid, 'shot three': three, 'post fade': fade, 'steal': stl}

def skill_control_inputter(handles, dish, dext, post_off, post_def, peri_def,):
    return {'ball handling': handles, 'passing': dish, 'dexterity': dext, 'post offense': post_off, 'perimeter defense': peri_def }

def skill_IQ_inputter(pick_set, pick_read, off_aware, def_aware):
    return {'screen setting': pick_set, 'screen using': pick_read, 'offensive awareness': off_aware, 'defensive awareness': def_aware}

def skill_athleticism_inputter(speed, strength, accel, jump, stamina):
    return {'speed': speed, 'strength': strength, 'acceleration': accel, 'jumping':jump, 'stamina':stamina}


#   1.2.2 --Actually create players--
player1 = Player('Dwayne "The Low Block" Johnson', 18, 'PF', trait_inputter(95,90,95,99), 76, 260, 77, 
                skill_inside_inputter(82, 67, 50, 70, 65, 90, 88), skill_outside_inputter(66,60,55,70), 
                skill_control_inputter(50,70,75,60,80,70), skill_IQ_inputter(90, 25, 60, 85), 
                skill_athleticism_inputter(60,95,65,65,88))

#print(player1.bball_skill_athleticism)



#2.---SIMULATE SEASONS---

seasons = 0

while seasons <10:
    player1.player_ager()
    player1.teen_grower()
    seasons+=1


print(player1.bball_skill_IQ['screen setting'])