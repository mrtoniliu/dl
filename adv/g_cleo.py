import adv_test
from adv import *
from slot import *
from slot.w import *
from slot.a import *
from slot.d import *
from module.fsalt import *

import random
random.seed()


def module():
    return G_Cleo

class G_Cleo(Adv):
    comment = '(the true cleo is here)'
    a3 = ('prep','100%')
    

    def d_slots(this):
        this.slots.a = RR()+JotS()  # wand c2*1.08 = 217
        this.slots.d = Shinobi()


    def d_acl(this):
        if 'blade' in this.ex:
            pass
        if this.condition('always in a1'):
            this.conf['acl'] = """
                `rotation
                """
            if 'bow' in this.ex:
                this.conf['rotation_init'] = """
                    s2s1
                """
                this.conf['rotation'] = """
                    c5c4fss1
                    c5s2c4fss1
                """
            else:
                this.conf['rotation_init'] = """
                    s2s1
                    c5c4fss1
                """
                this.conf['rotation'] = """
                    c5c4fss1
                    c5s2c5fss1
                """
              #  this.conf['rotation_init'] = """
              #      s2s1
              #  """
              #  this.conf['rotation'] = """
              #      c5c4fss1
              #      c5c5s2fss1
              #  """


    def prerun(this):
        this.s1p = 0 
        this.fsa_charge = 0
        #this.fso_dmg = this.conf.fs.dmg
        #this.fso_sp = this.conf.fs.sp

        this.fsaconf = Conf()
        this.fsaconf.fs = Conf(this.conf.fs)
        this.fsaconf({
                'fs.dmg':0,
                'fs.sp' :0,

                "fs.startup":43/60.0,
                "x5fs.startup":57/60.0,

                "fs.recovery":67/60.0,
                })
        this.fs_alt = Fs_alt(this, this.fsaconf)


        

    def s1_dmg(this, t):
        this.dmg_make('s1_hit_single',0.88)
        this.dmg_make('s1_hit_aoe',2.65)

    def s1_proc(this, e):
        this.s1p += 1
        if this.s1p > 3 :
            this.s1p = 1

        if this.s1p == 1:
            Timer(this.s1_dmg).on((42.0 + 12*0 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*1 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*2 )/60)
        elif this.s1p == 2:
            Timer(this.s1_dmg).on((42.0 + 12*0 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*1 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*2 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*3 )/60)
        elif this.s1p == 3:
            Timer(this.s1_dmg).on((42.0 + 12*0 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*1 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*2 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*3 )/60)
            Timer(this.s1_dmg).on((42.0 + 12*4 )/60)

        this.fs_alt.on()
        #this.conf.fs.dmg = 0
        #this.conf.fs.sp = 0
        this.fsa_charge = 1


    def fs_proc(this, e):
        if this.fsa_charge:
            #this.conf.fs.dmg = this.fso_dmg
            #this.conf.fs.sp = this.fso_sp
            this.fsa_charge = 0
            this.fs_alt.off()
            # ground buff doesnt affect by buff time, so use -debuff to emulate that.
            Debuff('a1_str',-0.25,10,1,'att','buff').on()



if __name__ == '__main__':
    conf = {}
    #module().comment = 'RR+SS'
    #conf['slots.a'] = RR()+FoG()

    conf['acl'] = """
        `s2
        `s1
        """

    adv_test.test(module(), conf, verbose=0)

