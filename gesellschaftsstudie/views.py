from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils import timezone
import time, random
from datetime import datetime, timedelta
from django.utils.timezone import activate

class abs1_hintergrund(Page):
    form_model = models.Player
    form_fields = ['gender', 'age', 'married', 'children', 'household']

    def get_form_fields(self):
        return ["gender",
                "age",
                "married",
                "children",
                "household",
                ]

class abs1_wohnort(Page):
    form_model = models.Player
    form_fields = ['bundesland','village', 'residencetime', 'neighborsmoving']

    def get_form_fields(self):
        return ["bundesland",
                "village",
                "residencetime",
                "neighborsmovingout",
                "neighborsmovingin",
                ]


class abs1_btw(Page):
    form_model = models.Player
    form_fields = ['election']

    def get_form_fields(self):
        return ["election",
                ]


class abs1_wahl1(Page):
    form_model = models.Player
    form_fields = ['party']

    def get_form_fields(self):
        return ["party",
                ]

    # def is_displayed(self):
    #    return self.participant.vars['election'] == 1

class abs1_wahl2(Page):
    form_model = models.Player
    form_fields = ['partyif']

    def get_form_fields(self):
        return ["partyif",
                ]

     # def is_displayed(self):
     #    return self.participant.vars['election'] == 2

class abs2_zeitung1(Page):
    pass


class abs2_zeitung2(Page):
    form_model = models.Player
    form_fields = ['manipulationcheck']

    def get_form_fields(self):
        return ["manipulationcheck",
                ]

class abs2_parteien(Page):
    form_model = models.Player
    form_fields = ['afd']

    def get_form_fields(self):
        return ["afd",
                ]

class abs2_petition(Page):
    form_model = models.Player
    form_fields = ['petition']

    def get_form_fields(self):
        return ["petition",
                ]

class abs3_politik(Page):
    form_model = models.Player
    form_fields = ['populism1', 'populism1']

    def get_form_fields(self):
        return ["populism1",
        "populism2",
                ]

class abs3_deutschland(Page):
    form_model = models.Player
    form_fields = ['nationalism1','nationalism2', 'nationalism3']

    def get_form_fields(self):
        return ["nationalism1",
        "nationalism2",
        "nationalism3",
                ]

class abs3_sozialstaat(Page):
    form_model = models.Player
    form_fields = ['rightwing1', 'rightwing2']

    def get_form_fields(self):
        return ["rightwing1",
        "rightwing2",
                ]

class abs3_kinder(Page):
    form_model = models.Player
    form_fields = ['authoritarian1', 'authoritarian2', 'authoritarian3', 'authoritarian4']

    def get_form_fields(self):
        return [
        "authoritarian1",
        "authoritarian2",
        "authoritarian3",
        "authoritarian4",
                ]
class abs3_meinung(Page):
    form_model = models.Player
    form_fields = ['immposi1', 'immposi2']

    def get_form_fields(self):
        return ["immposi1",
        "immposi2",
                ]

class abs3_personengruppen(Page):
    form_model = models.Player
    form_fields = ['attdiff1', 'attdiff2', 'attdiff3', 'attdiff4', 'attdiff5', 'attdiff6']

    def get_form_fields(self):
        return ["attdiff1",
        "attdiff2",
        "attdiff3",
        "attdiff4",
        "attdiff5",
        "attdiff6",
                ]

class abs3_fluchtlinge1(Page):
    form_model = models.Player
    form_fields = ['asylchance1','asylchance2', 'asylchance3', 'asylchance4' ]

    def get_form_fields(self):
        return ["asylchance1",
        "asylchance2",
        "asylchance3",
        "asylchance4",
            ]

class abs3_fluchtlinge2(Page):
    form_model = models.Player
    form_fields = ['asyl1','asyl2', 'asyl3', 'asyl4']

    def get_form_fields(self):
        return ["asyl1",
        "asyl2",
        "asyl3",
        "asyl4",
            ]

class abs5_ausland1(Page):
    form_model = models.Player
    form_fields = ['percentageforeignbula','percentageforeignvillage', 'aquaintances']

    def get_form_fields(self):
        return ["percentageforeignbula",
        "percentageforeignvillage",
        "aquaintances",
            ]

class abs5_ausland1(Page):
    form_model = models.Player
    form_fields = ['aquaintancesrefugees']

    def get_form_fields(self):
        return ["aquaintancesrefugees",
            ]

class abs5_kontakt1(Page):
    form_model = models.Player
    form_fields = ['refugees','contactrefugees']

    def get_form_fields(self):
        return ["refugees",
        "contactrefugees",
            ]

class abs5_kontakt2(Page):
    form_model = models.Player
    form_fields = ['contactrefugeesplace']

    def get_form_fields(self):
        return ["contactrefugeesplace",
            ]

     # def is_displayed(self):
     #    return self.participant.vars['contactrefugees'] == Ja

class abs5_fluchtlinge1(Page):
    form_model = models.Player
    form_fields = ['supportrefugees1','supportrefugees2']

    def get_form_fields(self):
        return ["supportrefugees1",
        "supportrefugees2",
            ]

class abs5_fluchtlinge2(Page):
    form_model = models.Player
    form_fields = ['againstrefugees','understandcontraref','understandproref']

    def get_form_fields(self):
        return ["againstrefugees",
        "understandcontraref",
        "understandproref",
            ]

class abs5_einstellung(Page):
    form_model = models.Player
    form_fields = ['feelingforeign','politicians','splitcommunity', 'sympathy']

    def get_form_fields(self):
        return ["feelingforeign",
        "politicians",
        "splitcommunity",
        "sympathy"
            ]


class abs5_sicherheit(Page):
    form_model = models.Player
    form_fields = ['fearalone','fearviolence','feartheft']

    def get_form_fields(self):
        return ["fearalone",
        "fearviolence",
        "feartheft"
            ]

class abs5_situation(Page):
    form_model = models.Player
    form_fields = ['ownfinancial','fairshare','loserside', 'secondclass']

    def get_form_fields(self):
        return ["ownfinancial",
        "fairshare",
        "loserside",
        "secondclass"
            ]

class abs5_nachbarn(Page):
    form_model = models.Player
    form_fields = ['neighborpoles','neighborturks','neighborsyrian', 'neighbornigerian']

    def get_form_fields(self):
        return ["neighborpoles",
        "neighborturks",
        "neighborsyrian",
        "neighbornigerian",
            ]

class abs5_heiraten(Page):
    form_model = models.Player
    form_fields = ['familypoles','familyturks','familysyrian', 'familynigerian' ]

    def get_form_fields(self):
        return ["familypoles",
        "familyturks",
        "familysyrian",
        "familynigerian",
            ]

class abs5_muslime(Page):
    form_model = models.Player
    form_fields = ['muslim1','muslim2']

    def get_form_fields(self):
        return ["muslim1",
        "muslim2",
            ]

class abs5_beruf(Page):
    form_model = models.Player
    form_fields = ['education','employed']

    def get_form_fields(self):
        return ["education",
        "employed",
            ]

class abs5_erwerbstatigkeit(Page):
    form_model = models.Player
    form_fields = ['notemployed']

    def get_form_fields(self):
        return ["notemployed",
            ]

     # def is_displayed(self):
     #    return self.participant.vars['employed'] == 4

class abs5_haushaltseinkommen(Page):
    form_model = models.Player
    form_fields = ['income']

    def get_form_fields(self):
        return ["income",
            ]

class abs5_religion(Page):
    form_model = models.Player
    form_fields = ['religion']

    def get_form_fields(self):
        return ["religion",
            ]

class abs5_migrationshintergrund(Page):
    form_model = models.Player
    form_fields = ['selfmigrant', 'selfvertrieben']

    def get_form_fields(self):
        return ["selfmigrant",
            "selfvertrieben",
            ]

class abs5_interesse(Page):
    form_model = models.Player
    form_fields = ['politics', 'rightleft']

    def get_form_fields(self):
        return ["politics",
            "rightleft",
            ]

class abs5_vertrauen(Page):
    form_model = models.Player
    form_fields = ['wallet', 'trustneighbor', 'communitybelonging']

    def get_form_fields(self):
        return ["wallet",
            "trustneighbor",
            "communitybelonging"
            ]


page_sequence = [
    abs1_hintergrund,
    abs1_wohnort,
    abs1_btw,
    abs1_wahl1,
    abs1_wahl2,
    abs2_zeitung1,
    abs2_zeitung2,
    abs2_parteien,
    abs2_petition,
    abs3_politik,
    abs3_deutschland,
    abs3_sozialstaat,
    abs3_kinder,
    abs3_meinung,
    abs3_personengruppen,
    abs3_fluchtlinge1,
    abs3_fluchtlinge2,
    abs5_ausland1,
    abs5_ausland1,
    abs5_kontakt1,
    abs5_kontakt2,
    abs5_fluchtlinge1,
    abs5_fluchtlinge2,
    abs5_einstellung,
    abs5_sicherheit,
    abs5_situation,
    abs5_nachbarn,
    abs5_heiraten,
    abs5_muslime,
    abs5_beruf,
    abs5_erwerbstatigkeit,
    abs5_haushaltseinkommen,
    abs5_religion,
    abs5_migrationshintergrund,
    abs5_interesse,
    abs5_vertrauen
]
