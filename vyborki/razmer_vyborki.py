from scipy import stats
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import zt_ind_solve_power

def ravenstvo_srednego(alpha, power, effect, std):
    """
    Определение размера выборки
    для проведения теста равенства среднего
    Принимает:
    * alpha - уровень значимости (вероятность ошибки первого рода)
    * power - мощность теста (вероятность ошибки второго рода)
    * effect - ожидаемый эффект
    * std - стандартное отклонение
    Выводит необходимый размер выборки
    """

    t_alpha = stats.norm.ppf(1 - alpha / 2, loc = 0, scale = 1)
    t_beta = stats.norm.ppf(power, loc = 0, scale = 1)
    var = 2 * std ** 2
    sample_size = int((t_alpha + t_beta) ** 2 * var / (effect ** 2))

    print('Необходимый размер выборки -', sample_size)


def ravenstvo_doley(alpha, power, p1, p2):
    """
    Определение размера выборки
    для проведения теста равенства долей
    Принимает:
    * alpha - уровень значимости (вероятность ошибки первого рода)
    * power - мощность теста (вероятность ошибки второго рода)
    * p1 - доля событий до вмешательства
    * p2 - ожидаемая доля после вмешательства 
    Выводит необходимый размер выборки
    """

    effect_size = proportion_effectsize(p1, p2)
    sample_size = zt_ind_solve_power(effect_size = effect_size, 
                                     alpha = alpha, 
                                     power = power)

    print('Необходимый размер выборки -', sample_size)
