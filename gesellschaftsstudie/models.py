from otree.api import (
    models, widgets, BaseConstants, BaseSubsession,
    BaseGroup, BasePlayer, Currency as c, currency_range,
)

from django.db.migrations.loader import MigrationLoader
from django.db.migrations.autodetector import MigrationAutodetector
from django.utils import timezone

import random



author = 'Johanna Gereke, Max Schaub'

doc = """
Gesellschaftsstudie
"""


class Constants(BaseConstants):
    name_in_url = 'gss'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number==1:
            random_sequence =list(range(1,1001))
            random.shuffle(random_sequence)
            self.session.vars['random_sequence'] = random_sequence
        for i, p in enumerate(self.get_players()):
            p.random_id = self.session.vars['random_sequence'][i]

class Group(BaseGroup):

    selected_individual_task = models.PositiveIntegerField()
    selected_pgg = models.PositiveIntegerField

class Player(BasePlayer):

    choices = models.CharField(
            widget=widgets.RadioSelect(attrs={'readonly':'readonly'}),
    )

    #Pre Survey Questions

    gender = models.CharField(choices=['Weiblich', 'Männlich'])

    age = models.PositiveIntegerField(min=18, max=99)

    married = models.PositiveIntegerField(choices=[
        [1, 'Verheiratet und leben mit Ihrem Ehepartner zusammen'],
        [2, 'Verheiratet und leben getrennt'],
        [3, 'Verwitwet'],
        [4, 'Geschieden'],
        [5, 'Ledig'],
        ],
        )

    children = models.PositiveIntegerField(choices=[
        [1,'Nein'],
        [2,'Ja, 1 Kind'],
        [3,'Ja, 2 Kinder'],
        [4,'Ja, 3 Kinder oder mehr'],
        ],
        )

    household = models.PositiveIntegerField(choices=[
        [1,'Nein, lebe allein'],
        [2,'Ja, noch 1 andere Person'],
        [3,'Ja, noch 2 andere Personen'],
        [4,'Ja, noch 3 andere Personen'],
        [5,'Ja, mehr als 3 andere Personen'],
        ],
        )

    bundesland = models.PositiveIntegerField(choices=[
        [1,'Baden-Württemberg'],
        [2,'Bayern'],
        [3,'Berlin'],
        [4,'Bremen'],
        [5,'Brandenburg'],
        [6,'Hamburg'],
        [7,'Hessen'],
        [8,'Mecklenburg-Vorpommern'],
        [9,'Niedersachsen'],
        [10,'Nordrhein-Westfalen'],
        [11,'Rheinland-Pfalz'],
        [12,'Saarland'],
        [13,'Sachsen'],
        [14,'Sachsen-Anhalt'],
        [15,'Schleswig-Holstein'],
        [16,'Thüringen'],

        ],
        )

    village = models.CharField()

    residencetime = models.PositiveIntegerField(choices=[
        [1, 'weniger als 1 Jahr'],
        [2, '1-3 Jahren'],
        [3, '4-10 Jahren'],
        [4, 'seit mehr 10 oder mehr Jahren'],
        ],
        )

    neighborsmovingout = models.PositiveIntegerField(choices=[
        [1, 'Keine Nachbarn sind weggezogen'],
        [2, '1-3 Nachbarn sind weggezogen'],
        [3, '4-10 Nachbarn sind weggezogen'],
        [4, '11 oder mehr  Nachbarn sind weggezogen'],
        [5, 'Weiß nicht/']
        ],
        )

    neighborsmovingin = models.PositiveIntegerField(choices=[
        [1, 'Keine Nachbarn sind hergezogen'],
        [2, '1-3 Nachbarn sind hergezogen'],
        [3, '4-10 Nachbarn sind hergezogen'],
        [4, '11 oder mehr  Nachbarn sind hergezogen'],
        [5, 'Weiß nicht/']
        ],
        )

    election = models.PositiveIntegerField(choices=[
        [1, 'ja, habe gewählt '],
        [2, 'nein, habe nicht gewählt'],
        ],
        )

    party = models.PositiveIntegerField(choices=[
        [1, 'CDU'],
        [2, 'SPD'],
        [3, 'DIE LINKE'],
        [4, 'AfD'],
        [5, 'FDP'],
        [6, 'DIE GRÜNEN'],
        [7, 'NPD '],
        [8, 'andere Partei'],
        ],
        )

    partyif = models.PositiveIntegerField(choices=[
        [1, 'CDU'],
        [2, 'SPD'],
        [3, 'DIE LINKE'],
        [4, 'AfD'],
        [5, 'FDP'],
        [6, 'DIE GRÜNEN'],
        [7, 'NPD '],
        [8, 'andere Partei'],
        ],
        )

    afd = models.PositiveIntegerField(choices=[
        [1, '-5, halte überhaupt nichts von dieser Partei'],
        [2, '-4'],
        [3, '-3'],
        [4, '-2'],
        [5, '-1'],
        [6, '0'],
        [7, '+1'],
        [8, '+2'],
        [9, '+3'],
        [10, '+4'],
        [11, '+5, halte sehr viel von dieser Partei '],
        [11, 'keine Angabe'],
        ],
    )

    manipulationcheck = models.PositiveIntegerField(choices=[
        [1,'1, entsprechen voll meiner persönlichen Wahrnehmung'],
        [2,'2'],
        [3,'3'],
        [4,'4'],
        [5,'5'],
        [6,'6'],
        [7,'7, entsprechen gar nicht meiner persönlichen Wahrnehmung'],
        [8,'keine Angabe'],
        ],
        )

    petition = models.PositiveIntegerField(choices=[
        [1, 'ja, ich möchte die Petition unterzeichnen'],
        [2, 'nein, ich möchte die Petition nicht unterzeichnen'],
        [3, 'keine Angabe'],
        ],
        )

    populism1 = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
    )

    populism2 = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
    )

    nationalism1 = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
    )

    nationalism2 = models.PositiveIntegerField(choices=[
        [1,'Sehr zufrieden'],
        [2,'Zufrieden'],
        [3,'Teils zufrieden/teils unzufrieden'],
        [4,'Unzufrieden'],
        [5,'Sehr unzufrieden'],
        [6,'Weiß nicht/ keine Angabe'],
        ],
    )
    nationalism3 = models.PositiveIntegerField(choices=[
        [1,'überhaupt nicht stolz'],
        [2,'nicht sehr stolz'],
        [3,'ziemlich stolz'],
        [4,'sehr stolz darauf sind'],
        ],
    )

    rightwing1 = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
    )
    rightwing2 = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    authoritarian1 = models.PositiveIntegerField(choices=[
        [1,'Unabhängigkeit'],
        [2,'Achtung vor älteren Menschen '],
        [3,'weiß nicht'],
        ],
    )

    authoritarian2 = models.PositiveIntegerField(choices=[
        [1,'Neugier'],
        [2,'Gutes Benehmen'],
        [3,'weiß nicht'],
        ],
    )
    authoritarian3 = models.PositiveIntegerField(choices=[
        [1,'Gehorsam'],
        [2,'Eigenständigkeit'],
        [3,'weiß nicht'],
        ],
    )

    authoritarian4 = models.PositiveIntegerField(choices=[
        [1,'Rücksichtsvoll'],
        [2,'Wohlerzogen'],
        [3,'weiß nicht'],
        ],
    )

    immposi1 = models.PositiveIntegerField(choices=[
        [1,'1, stimme überhaupt nicht zu'],
        [2,'2'],
        [3,'3'],
        [4,'4'],
        [5,'5'],
        [6,'6'],
        [7,'7, stimme voll und ganz zu'],
        [8,'keine Angabe'],
        ],
    )

    immposi2 = models.PositiveIntegerField(choices=[
        [1,'1, stimme überhaupt nicht zu'],
        [2,'2'],
        [3,'3'],
        [4,'4'],
        [5,'5'],
        [6,'6'],
        [7,'7, stimme voll und ganz zu'],
        [8,'keine Angabe'],
        ],
    )

    attdiff1 = models.PositiveIntegerField(choices=[
        [1,'Der Zuzug soll uneingeschränkt möglich sein'],
        [2,'Der Zuzug soll begrenzt werden'],
        [3,'Der Zuzug soll völlig unterbunden werden'],
        [4,'weiß nicht'],
        ],
    )

    attdiff2 = models.PositiveIntegerField(choices=[
        [1,'Der Zuzug soll UNEINGESCHRÄNKT möglich sein'],
        [2,'Der Zuzug soll BEGRENZT werden'],
        [3,'Der Zuzug soll völlig UNTERBUNDEN werden'],
        [4,'weiß nicht'],
        ],
    )

    attdiff3 = models.PositiveIntegerField(choices=[
        [1,'Der Zuzug soll UNEINGESCHRÄNKT möglich sein'],
        [2,'Der Zuzug soll BEGRENZT werden'],
        [3,'Der Zuzug soll völlig UNTERBUNDEN werden'],
        [4,'weiß nicht'],
        ],
    )

    attdiff4 = models.PositiveIntegerField(choices=[
        [1,'Der Zuzug soll UNEINGESCHRÄNKT möglich sein'],
        [2,'Der Zuzug soll BEGRENZT werden'],
        [3,'Der Zuzug soll völlig UNTERBUNDEN werden'],
        [4,'weiß nicht'],
        ],
    )

    attdiff5 = models.PositiveIntegerField(choices=[
        [1,'Der Zuzug soll UNEINGESCHRÄNKT möglich sein'],
        [2,'Der Zuzug soll BEGRENZT werden'],
        [3,'Der Zuzug soll völlig UNTERBUNDEN werden'],
        [4,'weiß nicht'],
        ],
    )

    attdiff6 = models.PositiveIntegerField(choices=[
        [1,'Der Zuzug soll UNEINGESCHRÄNKT möglich sein'],
        [2,'Der Zuzug soll BEGRENZT werden'],
        [3,'Der Zuzug soll völlig UNTERBUNDEN werden'],
        [4,'weiß nicht'],
        ],
    )

    asylchance1 = models.CharField(choices=['Ja, ist eine Chance', 'Nein', 'Weiß nicht'])
    asylchance2 = models.CharField(choices=['Ja, ist eine Chance', 'Nein', 'Weiß nicht'])
    asylchance3 = models.CharField(choices=['Ja, ist eine Chance', 'Nein', 'Weiß nicht'])
    asylchance4 = models.CharField(choices=['Ja, ist eine Chance', 'Nein', 'Weiß nicht'])

    asyl1 = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    asyl2 = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    asyl3 = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    asyl4 = models.PositiveIntegerField(choices=[
        [1,'Ja, habe ich'],
        [2,'Nein, habe ich nicht'],
        [3,'Weiß nicht/ keine Angabe'],
        ],
        )

    percentageforeignbula = models.CharField(blank = True)

    percentageforeignvillage = models.PositiveIntegerField(choices=[
        [1,'Nein, es gibt keine.'],
        [2,'ca. 1-10 Einzelpersonen'],
        [3,'ca. 11-50 Einzelpersonen'],
        [4,'ca. 51-100 Einzelpersonen'],
        [5,'101-199 Einzelpersonen'],
        [6,'Mehr als 200 Einzelpersonen'],
        [6,'Mehr als 1000 Einzelpersonen'],
        ],
        )

    aquaintances = models.PositiveIntegerField(choices=[
        [1,'niemand'],
        [2,'1-3'],
        [3,'4-5'],
        [4,'mehr als 5'],
        ],
        )

    aquaintancesrefugees = models.CharField(choices=['Ja', 'Nein', 'Weiß nicht'])

    refugees = models.CharField(choices=['Ja', 'Nein'])

    contactrefugees = models.CharField(choices=['Ja', 'Nein'])

    contactrefugeesplace = models.PositiveIntegerField(choices=[
        [1,'auf der Arbeit'],
        [2,'auf der Straße/im öffentlichen Raum'],
        [3,'in der Schule meiner Kinder'],
        [4,'im Verein'],
        [5,'als Freiwilliger'],
        [6,'bei offiziellen Treffen'],
        [7,'anderswo'],
        ],
        )

    supportrefugees1 = models.CharField(choices=['Ja', 'Nein', 'Weiß nicht'])

    supportrefugees2 = models.CharField(choices=['Ja', 'Nein', 'Weiß nicht'])

    againstrefugees = models.CharField(choices=['Ja', 'Nein', 'Keine Angabe'])

    understandcontraref = models.PositiveIntegerField(choices=[
       [1,'Ja, habe volles Verständnis'],
       [2,'Ja, habe etwas Verständnis'],
       [3,'Nein, habe kein Verständnis'],
       [4,'Nein, überhaupt kein Verständnis'],
       [5,'Weiß nicht/ keine Angabe'],
       ],
       )

    understandproref = models.PositiveIntegerField(choices=[
       [1,'Ja, habe volles Verständnis'],
       [2,'Ja, habe etwas Verständnis'],
       [3,'Nein, habe kein Verständnis'],
       [4,'Nein, überhaupt kein Verständnis'],
       [5,'Weiß nicht/ keine Angabe'],
       ],
       )


    feelingforeign = models.PositiveIntegerField(choices=[
       [1,'Stimme völlig zu'],
       [2,'Stimme überwiegend zu'],
       [3,'Lehne überwiegend ab'],
       [4,'Lehne völlig ab'],
       [5,'Weiß nicht/ keine Angabe'],
       ],
       )

    politicians = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    splitcommunity = models.PositiveIntegerField(choices=[
         [1,'Stimme völlig zu'],
         [2,'Stimme überwiegend zu'],
         [3,'Lehne überwiegend ab'],
         [4,'Lehne völlig ab'],
         [5,'Weiß nicht/ keine Angabe'],
         ],
         )


    sympathy  = models.PositiveIntegerField(choices=[
        [1,'Sehr viel'],
        [2,'Eher viel'],
        [3,'Eher wenig'],
        [4,'Wenig '],
        [5,'Weiß nicht/'],
        ],
        )

    fearalone  = models.PositiveIntegerField(choices=[
        [1,'Ja, gibt es hier'],
        [2,'Nein, gibt es hier nicht'],
        [3,'Weiß nicht/'],
        ],
        )

    feartheft = models.PositiveIntegerField(choices=[
        [1,'Höchst wahrscheinlich'],
        [2,'Eher wahrscheinlich'],
        [3,'Wahrscheinlich'],
        [4,'Eher unwahrscheinlich'],
        [5,'Völlig unwahrscheinlich'],
        [6,'Weiß nicht/'],
        ],
        )

    fearviolence = models.PositiveIntegerField(choices=[
        [1,'Höchst wahrscheinlich'],
        [2,'Eher wahrscheinlich'],
        [3,'Wahrscheinlich'],
        [4,'Eher unwahrscheinlich'],
        [5,'Völlig unwahrscheinlich'],
        [6,'Weiß nicht/'],
        ],
        )

    ownfinancial = models.PositiveIntegerField(choices=[
        [1,'Schlecht'],
        [2,'Weniger gut'],
        [3,'Gut'],
        [4,'Sehr gut'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    fairshare = models.PositiveIntegerField(choices=[
        [1,'Erhalte sehr viel weniger'],
        [2,'Erhalte etwas weniger'],
        [3,'Erhalte gerechten Anteil'],
        [4,'Erhalte weniger als gerechten Anteil'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    loserside = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    secondclass = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    neighborpoles = models.PositiveIntegerField(choices=[
        [1,'+3: wäre mir sehr angenehm'],
        [2,'+2 '],
        [3,'+1: eher angenehm'],
        [4,'0'],
        [5,'-1: eher unangenehm'],
        [6,'-2 '],
        [7,'-3: wäre mir sehr unangenehm'],
        [8,'Weiß nicht/ keine Angabe'],
        ],
        )

    neighborturks = models.PositiveIntegerField(choices=[
        [1,'+3, wäre mir sehr angenehm'],
        [2,'+2 '],
        [3,'+1, eher angenehm'],
        [4,'0'],
        [5,'-1, eher unangenehm'],
        [6,'-2 '],
        [7,'-3, wäre mir sehr unangenehm'],
        [8,'Weiß nicht/ keine Angabe'],
        ],
        )

    neighborsyrian = models.PositiveIntegerField(choices=[
        [1,'+3, wäre mir sehr angenehm'],
        [2,'+2 '],
        [3,'+1, eher angenehm'],
        [4,'0'],
        [5,'-1, eher unangenehm'],
        [6,'-2 '],
        [7,'-3, wäre mir sehr unangenehm'],
        [8,'Weiß nicht/ keine Angabe'],
        ],
        )

    neighbornigerian = models.PositiveIntegerField(choices=[
        [1,'+3, wäre mir sehr angenehm'],
        [2,'+2 '],
        [3,'+1, eher angenehm'],
        [4,'0'],
        [5,'-1, eher unangenehm'],
        [6,'-2 '],
        [7,'-3, wäre mir sehr unangenehm'],
        [8,'Weiß nicht/ keine Angabe'],
        ],
        )


    familypoles = models.PositiveIntegerField(choices=[
        [1,'+3, wäre mir sehr angenehm'],
        [2,'+2 '],
        [3,'+1, eher angenehm'],
        [4,'0'],
        [5,'-1, eher unangenehm'],
        [6,'-2 '],
        [7,'-3, wäre mir sehr unangenehm'],
        [8,'Weiß nicht/ keine Angabe'],
        ],
        )

    familyturks = models.PositiveIntegerField(choices=[
        [1,'+3, wäre mir sehr angenehm'],
        [2,'+2 '],
        [3,'+1, eher angenehm'],
        [4,'0'],
        [5,'-1, eher unangenehm'],
        [6,'-2 '],
        [7,'-3, wäre mir sehr unangenehm'],
        [8,'Weiß nicht/ keine Angabe'],
        ],
        )

    familysyrian = models.PositiveIntegerField(choices=[
        [1,'+3, wäre mir sehr angenehm'],
        [2,'+2 '],
        [3,'+1, eher angenehm'],
        [4,'0'],
        [5,'-1, eher unangenehm'],
        [6,'-2 '],
        [7,'-3, wäre mir sehr unangenehm'],
        [8,'Weiß nicht/ keine Angabe'],
        ],
        )

    familynigerian = models.PositiveIntegerField(choices=[
        [1,'+3, wäre mir sehr angenehm'],
        [2,'+2 '],
        [3,'+1, eher angenehm'],
        [4,'0'],
        [5,'-1, eher unangenehm'],
        [6,'-2 '],
        [7,'-3, wäre mir sehr unangenehm'],
        [8,'Weiß nicht/ keine Angabe'],
        ],
        )


    muslim1 = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Stimme nicht zu'],
        [4,'Stimme überhaupt nicht zu'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    muslim2 = models.PositiveIntegerField(choices=[
        [1,'Stimme völlig zu'],
        [2,'Stimme überwiegend zu'],
        [3,'Lehne überwiegend ab'],
        [4,'Lehne völlig ab'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    education = models.PositiveIntegerField(choices=[
        [1,'Schule beendet ohne Abschluss'],
        [2,'Hauptschulabschluss/ Volksschulabschluss'],
        [3,'Realschulabschluss/ Mittlere Reife'],
        [4,'Fachhochschulreife (Abschluss einer Fachoberschule)'],
        [5,'Abitur bzw. Hochschulreife '],
        [6,'noch in der Schule'],
        ],
        )

    employed = models.PositiveIntegerField(choices=[
        [1,'Vollzeit erwerbstätig'],
        [2,'Teilzeit erwerbstätig'],
        [3,'in Ausbildung/Studium'],
        [4,'nicht erwerbstätig'],
        [5,'trifft nicht zu'],
        [6,'keine Angabe'],
        ],
        )

    notemployed = models.PositiveIntegerField(choices=[
        [1,'in Rente, Pension oder im Vorruhestand'],
        [2,'Hausfrau/Hausmann'],
        [3,'Mutterschutz/Elternzeit'],
        [4,'arbeitslos (inkl. Ein-Euro-Jobs)'],
        [5,'aus anderen Gründen nicht berufstätig'],
        [6,'keine Angabe'],
        ],
        )

    religion = models.PositiveIntegerField(choices=[
        [1,'römisch-katholische Kirche '],
        [2,'evangelisch/protestantische Kirche'],
        [3,'andere Glaubensgemeinschaft'],
        [4,'keine Glaubensgemeinschaft '],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    selfmigrant = models.PositiveIntegerField(choices=[
        [1,'Ja'],
        [2,'Nein'],
        ],
        )

    selfvertrieben = models.PositiveIntegerField(choices=[
        [1,'Ja'],
        [2,'Nein'],
        ],
        )

    politics = models.PositiveIntegerField(choices=[
        [1,'sehr stark'],
        [2,'stark'],
        [3,'mittelmäßig'],
        [4,'weniger stark'],
        [5,'überhaupt nicht'],
        [6,'Weiß nicht/ keine Angabe'],
        ],
        )


    rightleft = models.PositiveIntegerField(choices=[
        [1,'1, links'],
        [2,'2'],
        [3,'3'],
        [4,'4'],
        [5,'5'],
        [6,'6'],
        [7,'7'],
        [8,'8'],
        [9,'9'],
        [10,'10, rechts'],
        [11,'Weiß nicht/ keine Angabe'],
        ],
        )

    wallet = models.PositiveIntegerField(choices=[
        [1,'höchst wahrscheinlich'],
        [2,'eher wahrscheinlich'],
        [3,'wahrscheinlich'],
        [4,'eher unwahrscheinlich'],
        [5,'völlig unwahrscheinlich'],
        [6,'Weiß nicht/ keine Angabe'],
        ],
        )

    trustneighbor = models.PositiveIntegerField(choices=[
        [1,'sehr stark'],
        [2,'stark'],
        [3,'mittelmäßig'],
        [4,'weniger stark'],
        [5,'überhaupt nicht'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    communitybelonging = models.PositiveIntegerField(choices=[
        [1,'Stark verbunden'],
        [2,'Ziemlich verbunden'],
        [3,'Wenig verbunden'],
        [4,'Gar nicht verbunden'],
        [5,'Weiß nicht/ keine Angabe'],
        ],
        )

    income = models.PositiveIntegerField(min=0, max=100000)
