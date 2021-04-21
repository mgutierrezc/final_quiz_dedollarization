from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# TODO: Chequear que los pagos mostrados al final sean la suma de los pagos en cada juego

class Survey(Page):
    form_model = 'player'
    form_fields = ['problems', 'problems_text', 'strategy',
                   'satisfaction_with_strat', 'understanding',
                   'understanding_text', 'age', 'gender',
                   'suggestions', 'eval_underst', 'ubicacion']

    def before_next_page(self): 
        self.group.set_payoffs()
        self.player.survey_timeout = int(self.participant.vars["player_left"])

    def is_displayed(self):
        # if self.participant.vars['MobilePhones'] is False and self.participant.vars['timed_out'] is False:
        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False

    def vars_for_template(self):
        language = self.session.config['language']
        return {'participant_id': self.participant.label, 'language': language}

"""
class SurveyInformation(Page): 

    def is_displayed(self):
        # if self.participant.vars['MobilePhones'] is False and self.player.survey_timeout == 0 and
        # self.participant.vars['timed_out'] == False:

        if self.participant.vars['MobilePhones'] is False:
            return True
        else:
            return False

    def vars_for_template(self):
        language = self.session.config['language']
        return {'language': language}


class Timed_Out(Page):
    timeout_seconds = Constants.timer

    def is_displayed(self):
        if self.participant.vars['MobilePhones'] is False and self.player.survey_timeout == 1:
            return True
        else:
            return False

    def vars_for_template(self):
        language = self.session.config['language']
        return {'language': language}

# Ver si se incluye hoja final de pagos o no

class FinalTaskResults(Page):
    def vars_for_template(self):
        pg_payoff = self.participant.vars['']
        return dict()


class PaymentInfo(Page):
    form_model = 'player'
    form_fields = ['aplicaciones_de_banco', 'nro_celular', 'nro_cuenta_bancaria',
                   'nro_cuenta_interbancaria', 'dni', 'banco_afiliado',
                   'nombre_titular', 'correo_paypal', 'celular_paypal',
                   'nombre_cuenta_paypal']

    def vars_for_template(self):
        language = self.session.config['language']
        return {'language': language}
"""


class LastPage(Page):
    def vars_for_template(self):
        language = self.session.config['language']
        return {'participant_id': self.participant.label, 'language': language}


page_sequence = [
    Survey,
    LastPage
]
