import adv_test
from adv import *
import copy
from module.fsalt import *


def module():
    return Albert


class Albert(Adv):
    comment = 'suitable skill prep; '
    a1 = ('fs',0.5)

    def init(this):
        if this.condition('big hitbox'):
            this.s1_proc = this.c_s1_proc


    def prerun(this):
        this.afflics.paralysis.maxdepth=15
        if this.condition('0 resist'):
            this.afflics.paralysis.resist=0
        else:
            this.afflics.paralysis.resist=100

        this.fsaconf = Conf()
        this.fsaconf.fs = Conf(this.conf.fs)
        this.fsaconf( {
                'fs.dmg':1.02,
                'fs.sp':330,
                'fs.recovery':26/60.0,
                'x1fs.recovery':26/60.0,
                })
        this.s2timer = Timer(this.s2autocharge,1,1).on()
        this.paralyze_count=3
        this.s2buff = Selfbuff("s2_shapshift",1, 20,'ss','ss')
        this.a3 = Selfbuff('a2_str_passive',0.25,20,'att','passive')

        this.fsalttimer = Timer(this.altend)
        fs_alt_init(this, this.fsaconf)

        if this.condition('4s1 in on s2'):
            this.conf['acl'] = """
                `s2, s1.charged>=s1.sp-300
                `s1
                `fs, seq=2 
                """

    def altend(this,t):
        fs_back(this)


    def s2autocharge(this, t):
        if not this.s2buff.get():
            this.s2.charge(160000.0/40)
            log('sp','s2autocharge')

            


    def c_s1_proc(this, e):
        if this.s2buff.get():
            this.dmg_make("o_s1_s2boost",12.38-0.825)
            this.dmg_make("o_s1_hit2", 0.83)
            this.dmg_make("o_s1_hit3", 0.83)
            this.dmg_make("o_s1_hit4", 0.83)
            this.dmg_make("o_s1_hit5", 0.83)
            this.dmg_make("o_s1_hit6", 0.83)
            this.s2buff.buff_end_timer.timing += 2.6
            this.a3.buff_end_timer.timing += 2.6
            this.s2timer.timing += 2.6
    

    def s1_proc(this, e):
        if this.s2buff.get():
            this.dmg_make("o_s1_s2boost",12.38-0.825)
            this.dmg_make("o_s1_hit2", 0.83)
            this.dmg_make("o_s1_hit3", 0.83)
            this.dmg_make("o_s1_hit4", 0.83)
            this.s2buff.buff_end_timer.timing += 2.6
            this.a3.buff_end_timer.timing += 2.6
            this.s2timer.timing += 2.6


    def fs_proc(this, e):
        if this.s2buff.get():
            this.afflics.paralysis('s2',100,0.803)

    def s2_proc(this, e):
        this.s2timer.on()
        this.s2buff.on()
        this.a3.on()
        fs_alt(this)
        this.fsalttimer(20)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s2
        `s1, this.s2.charged > 900
        `s3
        `fs, seq=2 and not this.s2buff.get()
        """

    import sys
    from slot.a import *
    if len(sys.argv) >= 3:
        sim_duration = int(sys.argv[2])
    else:
        sim_duration = 180
    if sim_duration == 60:
        #conf['slots.a'] = RR()+Worthy_Rivals()
        #conf['slots.a'] = TSO()+BBW()
        conf['slots.a'] = TSO()+Sisters_Day_Out()
    elif sim_duration == 90:
#        conf['slots.a'] = Heralds_of_Hinomoto()+The_Chocolatiers()
         conf['slots.a'] = TSO()+The_Chocolatiers()
    elif sim_duration == 120:
#        conf['slots.a'] = Heralds_of_Hinomoto()+The_Chocolatiers()
         conf['slots.a'] = TSO()+Sisters_Day_Out()
    elif sim_duration == 180:
        conf['slots.a'] = TSO()+Sisters_Day_Out()

    adv_test.test(module(), conf,verbose=0, mass=0)

