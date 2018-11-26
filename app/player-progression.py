import random
import statistics

#   ---CREATE PLAYER CLASS---
class Player:
    def __init__ (self, vitals, measurements, traits,
    threepoint_spotup, threepoint_creating, midrange_scoring, close_scoring, scoring_instincts, free_throw, driving_finesse,
    driving_strong, onballD_perimeter, onballD_post, team_defense, stealing, shot_defense, shot_blocking, rebounding,
    ball_handling, passing, post_control, lowpost_strong, lowpost_finesse, highpost, athleticism, years_pro, nonteen_yearsPro):
        
    #---DEFINE CLASS VARIABLES---

        #Bio
        self.vitals = vitals
        self.measurements = measurements
        self.traits = traits

        #Skillz
        self.threepoint_spotup = threepoint_spotup
        self.threepoint_creating = threepoint_creating
        self.midrange_scoring = midrange_scoring
        self.close_scoring = close_scoring
        self.scoring_instincts = scoring_instincts
        self.free_throw = free_throw
        self.driving_finesse = driving_finesse
        self.driving_strong = driving_strong
        self.onballD_perimeter = onballD_perimeter
        self.onballD_post = onballD_post
        self.team_defense = team_defense
        self.stealing = stealing
        self.shot_defense = shot_defense
        self.shot_blocking = shot_blocking
        self.rebounding = rebounding
        self.ball_handling = ball_handling
        self.passing = passing
        self.post_control = post_control
        self.lowpost_strong = lowpost_strong
        self.lowpost_finesse = lowpost_finesse
        self.highpost = highpost
        self.athleticism = athleticism

        #Status
        self.years_pro = years_pro
        self.nonteen_yearsPro = nonteen_yearsPro
        

    #---DEFINE CLASS FUNCTIONS---

    #**Age player**
    def player_ager(self):
        self.vitals['Age'] +=1
        self.years_pro +=1
        if self.vitals['Age'] > 20:
            self.nonteen_yearsPro +=1


    #**Grow teenage players**
    def teen_grower(self):
        growth_end_age = 20
        
        #Define growth rates
        potential_mental_growthRate = 0.33 * (self.traits['talent']*0.01)
        actual_mental_growthRate = potential_mental_growthRate * random.uniform((self.traits['training discipline (mental)']*0.01),1)
        
        potential_physical_growthRate = 0.09 * (self.traits['physical hardiness']*0.01)
        actual_physical_growthRate = potential_physical_growthRate * random.uniform((self.traits['training discipline (physical)']*0.01),1)
 
        #Apply growth
        if self.vitals['Age'] <= growth_end_age:
            self.scoring_instincts['Offensive consistency'] += (99 - self.scoring_instincts['Offensive consistency'])* actual_mental_growthRate
            self.scoring_instincts['Offensive consistency'] = int(round(self.scoring_instincts['Offensive consistency']))
            
            self.passing['Passing IQ'] += (99 - self.passing['Passing IQ']) * actual_mental_growthRate
            self.passing['Passing IQ'] = int(round(self.passing['Passing IQ']))

            self.team_defense['Pick and roll defense IQ'] += (99 - self.team_defense['Pick and roll defense IQ']) * actual_mental_growthRate
            self.team_defense['Pick and roll defense IQ'] = int(round(self.team_defense['Pick and roll defense IQ']))
            
            self.team_defense['Help defense IQ'] += (99 - self.team_defense['Help defense IQ']) * actual_mental_growthRate
            self.team_defense['Help defense IQ'] = int(round(self.team_defense['Help defense IQ']))

            self.team_defense['Defensive consistency'] += (99 - self.team_defense['Defensive consistency']) * actual_mental_growthRate
            self.team_defense['Defensive consistency'] = int(round(self.team_defense['Defensive consistency']))
            
            self.athleticism['Strength'] += (99 - self.athleticism['Strength']) * (actual_physical_growthRate) 
            self.athleticism['Strength'] = int(round(self.athleticism['Strength']))

            self.athleticism['Stamina'] += (99 - self.athleticism['Stamina']) * (actual_physical_growthRate) 
            self.athleticism['Stamina'] = int(round(self.athleticism['Stamina']))
        else:
           False
    

    #**Grow core skills of player**
    def coreSkills_grower(self):
    #---Define Core Growth Variables---
        #Player Traits
        attributes = list(player1.ball_handling.values()) + list(player1.close_scoring.values()) + list(player1.driving_finesse.values()) + list(player1.driving_strong.values()) + list(player1.free_throw.values()) + list(player1.highpost.values()) + list(player1.lowpost_finesse.values()) + list(player1.lowpost_strong.values()) + list(player1.midrange_scoring.values()) + list(player1.onballD_perimeter.values()) + list(player1.onballD_post.values()) + list(player1.passing.values()) + list(player1.post_control.values()) + list(player1.rebounding.values()) + list(player1.scoring_instincts.values()) + list(player1.shot_blocking.values()) + list(player1.shot_defense.values()) + list(player1.stealing.values()) + list(player1.team_defense.values()) #+ list(player1.threepoint_spotup.values())
        raw_potential = player1.traits['talent']
        discipline = player1.traits['training discipline (mental)']
        drive = player1.traits['drive']
        growth_rate = 2/3

        #Logic to adjust potential pool for each skill bucket 
        def drive_modifier(a, m):
            output = a * m
            if output <= 0.99:
                return output
            else:
                return 0.99 
        
        potential_pool_initial = 12
        potential_pool_elite = potential_pool_initial * raw_potential 
        potential_pool_strong = potential_pool_initial * raw_potential * drive_modifier(drive, 1.25)
        potential_pool_average = potential_pool_initial * raw_potential * drive_modifier(drive, 1.125)
        potential_pool_weak = potential_pool_initial * raw_potential * drive
        potential_pool_weakest = potential_pool_initial * raw_potential * drive
            
        potential_pool_initial_plus90 = 9
        potential_pool_elite_plus90 = potential_pool_initial_plus90 * raw_potential 
        potential_pool_strong_plus90 = potential_pool_initial_plus90 * raw_potential * drive_modifier(drive, 1.25)
        potential_pool_average_plus90 = potential_pool_initial_plus90 * raw_potential * drive_modifier(drive, 1.125)
        potential_pool_weak_plus90 = potential_pool_initial_plus90 * raw_potential * drive
        potential_pool_weakest_plus90 = potential_pool_initial_plus90 * raw_potential * drive


        #---Apply Growth by position---

        def PG_grower():
            #Discern cutoffs for skill buckets
            PG_core_ratings = list(player1.ball_handling.values()) + list(player1.close_scoring.values()) + list(player1.driving_finesse.values()) + list(player1.free_throw.values()) + list(player1.midrange_scoring.values()) + list(player1.onballD_perimeter.values()) + list(player1.passing.values()) + list(player1.shot_defense.values()) + list(player1.stealing.values()) + list(player1.team_defense.values()) + list(player1.threepoint_creating.values())
            PG_core_ratings.sort()
            PG_skill_len = len(PG_core_ratings) 
            PG_primary_divider = round(PG_skill_len/5)
            PG_eliteSkill_floor = PG_core_ratings[-PG_primary_divider]  #1st quartile
            PG_strongSkill_floor = PG_core_ratings[-PG_primary_divider * 2] #2nd quartile
            PG_avgSkill_floor = PG_core_ratings[-PG_primary_divider * 3] #3rd quartile ....
            PG_weakSkill_floor = PG_core_ratings[-PG_primary_divider * 4]
            PG_weakestSkill_floor = PG_core_ratings[0]


        def SG_grower():
        #---Define SG Growth Variables---
            #Core Skills of SG
            SG_core_skills = [self.ball_handling['Ball control'], self.ball_handling['Speed with ball'], self.close_scoring['Open shot closerange'], self.close_scoring['Off dribble shot closerange'], self.close_scoring['Contested shot closerange'], self.driving_finesse['Driving layup'], self.driving_strong['Driving dunk'], self.free_throw['Free throw'], self.highpost['Post fadeaway'], self.midrange_scoring['Open shot midrange'], self.midrange_scoring['Off dribble shot midrange'], self.midrange_scoring['Contested shot midrange'], self.onballD_perimeter['On ball defense IQ'], self.onballD_perimeter['Lateral quickness'], self.post_control['Post control'], self.post_control['Hands'], self.scoring_instincts['Shot IQ'], self.scoring_instincts['Draw foul'], self.scoring_instincts['Offensive consistency'], self.shot_defense['Shot contest'], player1.team_defense['Pick and roll defense IQ'], player1.team_defense['Help defense IQ'], player1.team_defense['Defensive consistency'], player1.threepoint_creating['Off dribble shot 3pt'], player1.threepoint_creating['Contested shot 3pt'], player1.threepoint_spotup['Open shot 3pt']]
            
            #Discern cutoffs for skill buckets
            SG_core_ratings = list(player1.ball_handling.values()) + list(player1.close_scoring.values()) + list(player1.driving_finesse.values()) + list(player1.driving_strong.values()) + list(player1.free_throw.values()) + list(player1.highpost.values()) + list(player1.midrange_scoring.values()) + list(player1.onballD_perimeter.values()) + list(player1.post_control.values()) + list(player1.scoring_instincts.values()) + list(player1.shot_defense.values()) + list(player1.team_defense.values()) + list(player1.threepoint_creating.values()) + list(player1.threepoint_spotup.values())
            SG_core_ratings.sort()
            SG_skill_len = len(SG_core_ratings) 
            SG_primary_divider = round(SG_skill_len/5)
            SG_eliteSkill_floor = SG_core_ratings[-SG_primary_divider]  #1st quartile
            SG_strongSkill_floor = SG_core_ratings[-SG_primary_divider * 2] #2nd quartile
            SG_avgSkill_floor = SG_core_ratings[-SG_primary_divider * 3] #3rd quartile ....
            SG_weakSkill_floor = SG_core_ratings[-SG_primary_divider * 4] 
            SG_weakestSkill_floor = SG_core_ratings[0]

            def growth_logic(attribute):
                #Logic determining potential, annual growth 
                potential_pool = 0     
                 
                if attribute >= SG_eliteSkill_floor:  
                    if attribute < 90:
                        potential_pool = potential_pool_elite
                    elif attribute >= 90:
                        potential_pool = potential_pool_elite_plus90
                elif attribute >= SG_strongSkill_floor and attribute < SG_eliteSkill_floor:
                    if attribute < 90:
                        potential_pool = potential_pool_strong
                    elif attribute >= 90:
                        potential_pool = potential_pool_strong_plus90
                elif attribute >= SG_avgSkill_floor and attribute < SG_strongSkill_floor:
                    if attribute < 90:
                        potential_pool = potential_pool_average
                    elif attribute >= 90:
                        potential_pool = potential_pool_average_plus90
                elif attribute >= SG_weakSkill_floor and attribute < SG_avgSkill_floor:
                    if attribute < 90:
                        potential_pool = potential_pool_weak
                    elif attribute >= 90:
                        potential_pool = potential_pool_weak_plus90
                elif attribute < SG_weakSkill_floor:
                    if attribute < 90:
                        potential_pool = potential_pool_weakest
                        
                annual_growth_ceiling = potential_pool * growth_rate
                annual_growth_actual = annual_growth_ceiling * discipline
                attribute += annual_growth_actual
                
                return attribute

            #---Apply SG Annual Growth---
            if self.vitals['Age'] > 20 and self.nonteen_yearsPro <= 3:
                SG_core_skills = list(map(growth_logic, SG_core_skills))
            else:
                False

            print(SG_core_skills, self.ball_handling['Ball control'])

        def SF_grower():
            SF_primary_skills = list(player1.close_scoring.values()) + list(player1.driving_finesse.values()) + list(player1.driving_strong.values()) + list(player1.free_throw.values()) + list(player1.highpost.values()) + list(player1.midrange_scoring.values()) + list(player1.onballD_perimeter.values()) + list(player1.scoring_instincts.values()) + list(player1.shot_defense.values()) + list(player1.stealing.values()) + list(player1.team_defense.values()) + list(player1.threepoint_spotup.values())
            SF_primary_skills.sort()
            SF_skill_len = len(SF_primary_skills) 
            SF_primary_divider = round(SF_skill_len/5)
            SF_eliteSkill_floor = SF_primary_skills[-SF_primary_divider]  #1st quartile
            SF_strongSkill_floor = SF_primary_skills[-SF_primary_divider * 2] #2nd quartile
            SF_avgSkill_floor = SF_primary_skills[-SF_primary_divider * 3] #3rd quartile ....
            SF_weakSkill_floor = SF_primary_skills[-SF_primary_divider * 4]
            SF_weakestSkill_floor = SF_primary_skills[0]

        def PF_grower():
            PF_primary_skills = list(player1.close_scoring.values()) + list(player1.driving_strong.values()) + list(player1.highpost.values()) + list(player1.midrange_scoring.values()) + list(player1.onballD_post.values()) + list(player1.post_control.values()) + list(player1.rebounding.values()) + list(player1.scoring_instincts.values()) + list(player1.shot_defense.values()) + list(player1.team_defense.values()) + list(player1.free_throw.values())
            PF_primary_skills.sort()
            PF_skill_len = len(PF_primary_skills) 
            PF_primary_divider = round(PF_skill_len/5)
            PF_eliteSkill_floor = PF_primary_skills[-PF_primary_divider]  #1st quartile
            PF_strongSkill_floor = PF_primary_skills[-PF_primary_divider * 2] #2nd quartile
            PF_avgSkill_floor = PF_primary_skills[-PF_primary_divider * 3] #3rd quartile ....
            PF_weakSkill_floor = PF_primary_skills[-PF_primary_divider * 4]
            PF_weakestSkill_floor = PF_primary_skills[0]

        def C_grower():
            C_primary_skills = list(player1.close_scoring.values()) + list(player1.lowpost_finesse.values()) + list(player1.lowpost_strong.values()) + list(player1.onballD_post.values()) + list(player1.post_control.values()) + list(player1.rebounding.values()) + list(player1.shot_blocking.values()) + list(player1.scoring_instincts.values()) + list(player1.shot_defense.values()) + list(player1.team_defense.values()) + list(player1.free_throw.values())
            C_primary_skills.sort()
            C_skill_len = len(C_primary_skills) 
            C_primary_divider = round(C_skill_len/5)
            C_eliteSkill_floor = C_primary_skills[-C_primary_divider]  #1st quartile
            C_strongSkill_floor = C_primary_skills[-C_primary_divider * 2] #2nd quartile
            C_avgSkill_floor = C_primary_skills[-C_primary_divider * 3] #3rd quartile ....
            C_weakSkill_floor = C_primary_skills[-C_primary_divider * 4]
            C_weakestSkill_floor = C_primary_skills[0]


        

        if player1.vitals['Position'] == 'PG':
            return PG_grower()
        elif player1.vitals['Position'] == 'SG':
            return SG_grower()
        elif player1.vitals['Position'] == 'SF':
            return SF_grower()
        elif player1.vitals['Position'] == 'PF':
            return PF_grower() 
        elif player1.vitals['Position'] == 'C':
            return C_grower()


           
        

        #print(SF_primary_skills, SF_eliteSkill_floor, SF_strongSkill_floor, SF_avgSkill_floor, SF_weakSkill_floor, SF_weakestSkill_floor)
        #print(PF_primary_skills, PF_eliteSkill_floor, PF_strongSkill_floor, PF_avgSkill_floor, PF_weakSkill_floor, PF_weakestSkill_floor)
        #print(C_primary_skills, C_eliteSkill_floor, C_strongSkill_floor, C_avgSkill_floor, C_weakSkill_floor, C_weakestSkill_floor)

#   1.2 --Create Instances of Player--

#   1.2.1 --Define attributes--
def vital_function(name, age, position):
    return {'Name': name, 'Age':age, 'Position': position}

def measurement_function(height, weight, wingspan):
    return {'Height (inches)': height, 'Weight':weight, 'Wingspan': wingspan}

def trait_function(talent, drive, mental_disc, phys_hard, phys_disc):
    return {'talent': talent * 0.01 , 'drive': drive * 0.01, 'training discipline (mental)': mental_disc * 0.01, 'physical hardiness': phys_hard * 0.01, 'training discipline (physical)': phys_disc * 0.1}

def threepoint_spotup_function(open_3):
    return {'Open shot 3pt': open_3}

def threepoint_create_function(offdribble_3, contested_3):
    return {'Off dribble shot 3pt': offdribble_3, 'Contested shot 3pt': contested_3}

def midrange_scoring_function(open_mid, offdribble_mid, contested_mid):
    return {'Open shot midrange': open_mid, 'Off dribble shot midrange': offdribble_mid, 'Contested shot midrange': contested_mid}

def closerange_scoring_function(open_close, offdribble_close, contested_close):
    return {'Open shot closerange': open_close, 'Off dribble shot closerange': offdribble_close, 'Contested shot closerange': contested_close}

def scoring_instincts_function(shot_IQ, draw_foul, off_consistency):
    return {'Shot IQ': shot_IQ, 'Draw foul':draw_foul, 'Offensive consistency': off_consistency}

def free_throw_function(free_throw):
    return {'Free throw': free_throw}

def driving_finesse_function(driving_layup):
    return {'Driving layup': driving_layup}

def driving_strong_function(driving_dunk):
    return {'Driving dunk': driving_dunk}

def onballD_perimeter_function(onball_D, lat_quick):
    return {'On ball defense IQ': onball_D, 'Lateral quickness': lat_quick}

def onballD_post_function(post_D):
    return {'Post defense': post_D}

def team_defense_function(PnR_def_IQ, help_def_IQ, def_consistency):
    return {'Pick and roll defense IQ': PnR_def_IQ, 'Help defense IQ': help_def_IQ, 'Defensive consistency': def_consistency}

def stealing_function(steal, pass_percept, rxn_time):
    return {'Steal': steal, 'Pass perception': pass_percept, 'Reaction time': rxn_time}

def shot_defense_function(shot_contest):
    return {'Shot contest': shot_contest}

def shot_blocking_function(shot_block):
    return {'Shot blocking': shot_block}

def rebounding_function(off_reb, def_reb, boxout):
    return {'Offensive rebound': off_reb, 'Defensive rebound': def_reb, 'Boxout': boxout}

def ball_handling_function(ball_control, speed_w_ball):
    return {'Ball control': ball_control, 'Speed with ball': speed_w_ball}

def passing_function(pass_accuracy, pass_IQ, pass_vision):
    return {'Pass accuracy': pass_accuracy, 'Passing IQ': pass_IQ, 'Passing vision': pass_vision}

def post_control_function(post_control, hands):
    return {'Post control': post_control, 'Hands': hands}

def lowpost_strong_function(stand_dunk, contact_dunk):
    return {'Standing dunk': stand_dunk, 'Contact dunk':contact_dunk}

def lowpost_finesse_function(stand_layup, hook):
    return {'Standing layup': stand_layup, 'Post hook': hook}

def highpost_function(post_fade):
    return {'Post fadeaway': post_fade}

def athleticism_function(speed, accel, vert, strength, stamina, hustle, durability):
    return {'Speed': speed, 'Acceleration': accel, 'Vertical': vert, 'Strength': strength, 'Stamina':stamina, 'Hustle': hustle, 'Durability': durability}

#def years_pro_function(years_pro, nonteen_years_pro):
    #return {'Years pro':years_pro, 'Non teen years pro': nonteen_years_pro}

# 
#  1.2.2 --Create players--
# 
#Take user inputs
# vital_input_name = input('Enter your player\'s name: ')
# vital_input_age = int(input('Enter your player\'s age: '))
# vital_input_position = input('Enter your player\'s position: ')
# 
# measurement_input_height = int(input('Enter your player\'s height: '))
# measurement_input_weight = int(input('Enter your player\'s weight: '))
# measurement_input_wingspan = int(input('Enter your player\'s wingspan: '))
# 
# trait_input_talent = int(input('Enter your player\'s talent: '))
# trait_input_drive = int(input('Enter your player\'s drive: '))
# trait_input_mentalDiscipline = int(input('Enter your player\'s training discipline (mental): '))
# trait_input_physHard = int(input('Enter your player\'s physical hardiness: '))
# trait_input_physDisc = int(input('Enter your player\'s training discipline (physical): '))
# 
# threepoint_input_scoring_open = int(input('Enter your player\'s Open Shot 3pt rating: '))
# threepoint_input_scoring_offDribble = int(input('Enter your player\'s Off-dribble Shot 3pt rating: '))
# threepoint_input_scoring_contested = int(input('Enter your player\'s Contested Shot 3pt rating: '))
# 
# midrange_input_scoring_open = int(input('Enter your player\'s Open Shot Midrange rating: '))
# midrange_input_scoring_offDribble = int(input('Enter your player\'s Off-dribble Shot Midrange rating: '))
# midrange_input_scoring_contested = int(input('Enter your player\'s Contested Shot Midrange rating: '))
# 
# close_input_scoring_open = int(input('Enter your player\'s Open Shot Close rating: '))
# close_input_scoring_offDribble = int(input('Enter your player\'s Off-dribble Shot Close rating: '))
# close_input_scoring_contested = int(input('Enter your player\'s Contested Shot Close rating: '))
# 
# scoring_instincts_input_shotIQ = int(input('Enter your player\'s Shot IQ rating: '))
# scoring_instincts_input_drawFoul = int(input('Enter your player\'s draw foul rating: '))
# scoring_instincts_input_offconsistency = int(input ('Enter your player\'s offensive consistency rating: '))
# 
# free_throw_input = int(input('Enter your player\'s free throw rating: '))
# 
# driving_finesse_input_drivinglayup = int(input('Enter your player\'s driving layup rating: '))
# 
# driving_strong_input_drivedunk = int(input('Enter your player\'s driving dunk rating: '))
# 
# onballD_perimeter_input_IQ = int(input('Enter your player\'s on ball defense IQ rating: '))
# onballD_perimeter_input_latquick = int(input('Enter your player\'s lateral quickness rating: '))
# onballD_post_input = int(input('Enter your player\'s post defense rating: '))
# 
# team_defense_input_PnR = int(input('Enter your player\'s pick and roll defense IQ rating: '))
# team_defense_input_help = int(input('Enter your player\'s help defense IQ rating: '))
# team_defense_input_consist = int(input('Enter your player\'s defensive consistency rating: '))
# 
# steal_input_stl = int(input('Enter your player\'s steal rating: '))
# steal_input_passPercept = int(input('Enter your player\'s pass perception rating: '))
# steal_input_rxn = int(input('Enter your player\'s reaction time rating: '))
# shotContest_input = int(input('Enter your player\'s shot contest rating: '))
# shotBlock_input = int(input('Enter your player\'s shot block rating: '))
# 
# rebounding_input_off = int(input('Enter your player\'s offensive rebounding rating: '))
# rebounding_input_def = int(input('Enter your player\'s defensive rebounding rating: '))
# rebounding_input_box = int(input('Enter your player\'s boxout rating: '))
# 
# ball_handling_input_control = int(input('Enter your player\'s ball control rating: '))
# ball_handling_input_speed = int(input('Enter your player\'s speed with ball rating: '))
# 
# passing_input_accuracy = int(input('Enter your player\'s passing accuracy rating: '))
# passing_input_IQ = int(input('Enter your player\'s passing IQ rating: '))
# passing_input_vision = int(input('Enter your player\'s passing vision rating: '))
# 
# post_input_control = int(input('Enter your player\'s post control rating: '))
# post_input_hands = int(input('Enter your player\'s hands rating: '))
# 
# lowpost_strong_input_standDunk = int(input('Enter your player\'s standing dunk rating: '))
# lowpost_strong_input_contactDunk = int(input('Enter your player\'s contact dunk rating: '))
# 
# lowpost_finesse_input_standLayup = int(input('Enter your player\'s standing layup rating: '))
# lowpost_finesse_input_hook = int(input('Enter your player\'s post hook rating: '))
# 
# highpost_finesse_input_fade = int(input('Enter your player\'s post fadeaway rating: '))
# 
# athleticism_input_speed = int(input('Enter your player\'s speed rating: '))
# athleticism_input_accel = int(input('Enter your player\'s acceleration rating: '))
# athleticism_input_vertical = int(input('Enter your player\'s vertical rating: '))
# athleticism_input_strength = int(input('Enter your player\'s strength rating: '))
# athleticism_input_stamina = int(input('Enter your player\'s stamina rating: '))
# athleticism_input_hustle = int(input('Enter your player\'s hustle rating: '))
# athleticism_input_durable = int(input('Enter your player\'s durability rating: '))
# 
#Create player
# player1 = Player(vital_function(vital_input_name, vital_input_age, vital_input_position),
    # measurement_function(measurement_input_height, measurement_input_weight, measurement_input_wingspan), 
    # trait_function(trait_input_talent, trait_input_drive, trait_input_mentalDiscipline,trait_input_physHard,trait_input_physDisc), 
    # threepoint_spotup_function(threepoint_input_scoring_open), threepoint_create_function(threepoint_input_scoring_offDribble, threepoint_input_scoring_contested),
    # midrange_scoring_function(midrange_input_scoring_open, midrange_input_scoring_offDribble, midrange_input_scoring_contested),
    # closerange_scoring_function(close_input_scoring_open, close_input_scoring_offDribble, close_input_scoring_contested), 
    # scoring_instincts_function(scoring_instincts_input_shotIQ, scoring_instincts_input_drawFoul, scoring_instincts_input_offconsistency), 
    # free_throw_function(free_throw_input), driving_finesse_function(driving_finesse_input_drivinglayup),
    # driving_strong_function(driving_strong_input_drivedunk), onballD_perimeter_function(onballD_perimeter_input_IQ, onballD_perimeter_input_latquick),
    # onballD_post_function(onballD_post_input), team_defense_function(team_defense_input_PnR, team_defense_input_help, team_defense_input_consist),
    # stealing_function(steal_input_stl, steal_input_passPercept, steal_input_rxn), shot_defense_function(shotContest_input),
    # shot_blocking_function(shotBlock_input), rebounding_function(rebounding_input_off,rebounding_input_def, rebounding_input_box),
    # ball_handling_function(ball_handling_input_control, ball_handling_input_speed), passing_function(passing_input_accuracy, passing_input_IQ, passing_input_vision),
    # post_control_function(post_input_control, post_input_hands), lowpost_strong_function(lowpost_strong_input_standDunk, lowpost_strong_input_contactDunk),
    # lowpost_finesse_function(lowpost_finesse_input_standLayup, lowpost_finesse_input_hook), highpost_function(highpost_finesse_input_fade), 
    # athleticism_function(athleticism_input_speed, athleticism_input_accel, athleticism_input_vertical, athleticism_input_strength, athleticism_input_stamina, athleticism_input_hustle, athleticism_input_durable),0,0
    # )

player1 = Player(vital_function('Allen Iverson', 18, 'SG'), measurement_function(72,160,72), trait_function(99, 45, 45, 70, 73), threepoint_spotup_function(70), threepoint_create_function(80, 82), midrange_scoring_function(80, 82, 83), 
   closerange_scoring_function(84, 87, 87), scoring_instincts_function(85, 72, 80), free_throw_function(70),driving_finesse_function(88), driving_strong_function(80),
   onballD_perimeter_function(73, 86), onballD_post_function(25), team_defense_function(65,70,80), stealing_function(85, 87, 86),
   shot_defense_function(70), shot_blocking_function(45), rebounding_function(30, 40, 35), ball_handling_function(90 , 90), passing_function(75, 75, 60),
   post_control_function(40, 80), lowpost_strong_function(40, 35), lowpost_finesse_function(70, 40), highpost_function(50),
   athleticism_function(97, 98, 94, 50, 97, 95, 90), 0, 0)



#---SIMULATE SEASONS---

#print(f'On draft day {player1.vitals['Name']} is {player1.age} years old, and his skill of offensive awareness is ' + str(int((player1.skill_IQ['offensive awareness']))))
#print('On draft day ' + str(player1.vitals['Name']) + 'is ' +str(player1.vitals['Age']) +' years old. He has ' + str(player1.nonteen_yearsPro) + ' non teenage years pro in the league.')


season = 0
printcounter = 0

while season <=10:
    
    if printcounter == 1:
    #   print(f'After season {season}, {player1.vitals['Name']} is {player1.age} years old, and his skill of offensive awareness is ' + str(int((player1.skill_IQ['offensive awareness']))))
        print('player age: ' + str(player1.vitals['Age']))
        
        #print('Offensive consistency: ' + str(player1.scoring_instincts['Offensive consistency']))
        printcounter = 0

    player1.coreSkills_grower()
    player1.player_ager()
    player1.teen_grower()
        
    printcounter+=1
    season+=1

