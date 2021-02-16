from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Marco Gutierrez'

doc = """
General Final Quiz - MTurk
"""


class Constants(BaseConstants):
    name_in_url = 'final_quiz'
    contact_template = 'dedollarization/Contactenos.html'
    players_per_group = None
    num_rounds = 1

    timer = 300

    survey_payoff = c(0)

    english_labels = dict(age='What is your age?', gender='What is your gender?',
                          strategy='Please describe the strategy that you used in making your decisions:',
                          problems='Did you encounter any problems while completing the task?',
                          problems_text='If so, please describe the problems you encountered:',
                          satisfaction_with_strat='You were satisfied with your strategy:',
                          understanding='You understood the whole study:',
                          understanding_text='If not, please explain:',
                          )
    spanish_labels = dict(age='¿Cuál es tu edad?', gender='¿Cuál es tu género?',
                          strategy='Por favor, describa la estrategia que usaste para tomar decisiones:',
                          problems='¿Encontraste algún problema cuando completaste la tarea?',
                          problems_text='De ser así, por favor describe los problemas encontrados:',
                          satisfaction_with_strat='¿Estuviste satisfecho con tu estrategia?',
                          understanding='¿Entendiste el estudio?',
                          understanding_text='Si no, describa por qué:',
                          )
    english_answers = dict(gender=[['Male', 'Male'], ['Female', 'Female']],
                           problems=[['Yes', 'Yes'], ['No', 'No']],
                           satisfaction_with_strat=[['Strongly Agree', 'Strongly Agree'], ['Agree', 'Agree'],
                                                    ['Neutral', 'Neutral'], ['Disagree', 'Disagree'],
                                                    ['Strongly Disagree', 'Strongly Disagree']],
                           understanding=[['Strongly Agree', 'Strongly Agree'], ['Agree', 'Agree'],
                                          ['Neutral', 'Neutral'], ['Disagree', 'Disagree'],
                                          ['Strongly Disagree', 'Strongly Disagree']],
                           )
    spanish_answers = dict(gender=[['Hombre', 'Hombre'], ['Mujer', 'Mujer'], ['Otro', 'Otro']],
                           problems=[['Sí', 'Sí'],['No', 'No']],
                           satisfaction_with_strat=[['Muy de Acuerdo', 'Muy de Acuerdo'], ['De Acuerdo', 'De Acuerdo'],
                                                    ['Neutral', 'Neutral'], ['En Desacuerdo', 'En Desacuerdo'],
                                                    ['Muy en Desacuerdo', 'Muy en Desacuerdo']],
                           understanding=[['Muy de Acuerdo', 'Muy de Acuerdo'], ['De Acuerdo', 'De Acuerdo'],
                                                    ['Neutral', 'Neutral'], ['En Desacuerdo', 'En Desacuerdo'],
                                                    ['Muy en Desacuerdo', 'Muy en Desacuerdo']],
                           )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def set_payoffs(self):
        for p in self.get_players():
            #  p.participant.vars['final_payoff'] += Constants.survey_payoff
            p.payoff = Constants.survey_payoff.to_real_world_currency(self.session)


class Player(BasePlayer):

    age = models.IntegerField(label=Constants.spanish_labels['age'], min=18, max=125)

    gender = models.StringField(
        choices= Constants.spanish_answers['gender'],
        label= Constants.spanish_labels['gender'],
        widget=widgets.RadioSelect,
    )

    survey_timeout = models.IntegerField(initial=0)

    total_earnings_dollar = models.CharField()
    
    strategy = models.LongStringField(label=Constants.spanish_labels['strategy'])

    problems = models.CharField(label=Constants.spanish_labels['problems']
    ,choices=Constants.spanish_answers['problems'], widget=widgets.RadioSelect)

    problems_text = models.LongStringField(label=Constants.spanish_labels['problems_text'],
    blank=True)

    satisfaction_with_strat = models.CharField(label=Constants.spanish_labels['satisfaction_with_strat']
                                               ,choices=Constants.spanish_answers['satisfaction_with_strat']
                                               ,widget=widgets.RadioSelect)

    understanding = models.CharField(label=Constants.spanish_labels['understanding'],
                                     choices=Constants.spanish_answers['understanding']
                                     ,widget=widgets.RadioSelect)

    understanding_text = models.LongStringField(label=Constants.spanish_labels['understanding_text'],
    blank=True)

    suggestions = models.LongStringField(label='Escribe tus sugerencias sobre el experimento', blank=True)

    quiz_earnings = models.CurrencyField()

    instruction_earnings = models.CurrencyField()

    game_earnings = models.CurrencyField()

    survey_earnings = models.CurrencyField()

    total_earnings = models.CurrencyField()

    banking_app = models.BooleanField(label='¿Tienes algun celular a una aplicacion de banca movil?',
                                      choices=[[False,'No'],[True, 'Sí']],
                                      widget=widgets.RadioSelect)

    aplicaciones_de_banco = models.IntegerField(label='Escoge tu medio de pago:',
                                                choices=[[0, 'Yape (BCP)'], [1, 'Lukita (BBVA)'],
                                                         [2, 'Tunki (Interbank)'],
                                                         [3, 'Transferencia Bancaria/Interbancaria'],
                                                         [4, 'Paypal']],
                                                widget=widgets.RadioSelect)

    nro_celular = models.StringField(label='Nro. de celular afiliado', blank=True)
    nro_cuenta_bancaria = models.StringField(label='Nro. de cuenta bancario', blank=True)
    nro_cuenta_interbancaria = models.StringField(label='Nro. de cuenta interbancario', blank=True)
    dni = models.StringField(label='Nro. de DNI del titular de la cuenta', blank=True)
    banco_afiliado = models.StringField(label='Banco afiliado a los pagos', blank=True)
    nombre_titular = models.StringField(label='Nombre de Cuenta', blank=True)
    correo_paypal = models.StringField(label='Correo Afiliado a PayPal', blank=True)
    celular_paypal = models.StringField(label='Celular Afiliado a PayPal', blank=True)
    nombre_cuenta_paypal = models.StringField(label='Nombre de Cuenta de PayPal', blank=True)
    ubicacion = models.CharField(label='¿En qué lugar has realizado el experimento?', choices=[
        ['Casa', 'Casa'], ['Cafe/Restaurant/Local Comercial', 'Cafe/Restaurant/Local Comercial'],
        ['Biblioteca', 'Biblioteca'], ['Cabina de Internet', 'Cabina de Internet'],
        ['Universidad', 'Universidad']])

    # Hidden field for quiz
    eval_underst = models.LongStringField(blank=True)
