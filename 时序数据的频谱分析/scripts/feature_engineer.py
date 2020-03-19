import tsfresh.feature_extraction.feature_calculators as tff
import pandas as pd

def features_extract(timeseries):

    '''
    :param timeseries: pd.Series, must be 1d
    :return: features, DataFrame, features of timeseries

    make sense:
    abs_energy:   绝对能量值
    app_entropy:  近似熵
    bin_entropy: 分组熵
    cwt_coef:    Ricker小波分析
    fft_agg:     Fuller变换的频谱统计量
    fft_coef:    Fuller变换系数
    abs_soc:     一阶差分绝对和
    agg_acor:    各阶自相关系数的聚合统计
    agg_liner:   分块时序聚合值得线性回归
    ar_coef:     自回归系数
    adf_test:    ADF检验
    cid_ce:      时序数据复杂度
    peak:       峰度
    mean_absc:  绝对差值的平均值
    mean_sdc:   二阶导数的中心的均值
    ncm:        零交叉的数量

    you can get details of feature using dictionary[key], such features['abs_energy']
    '''

    abs_energy = tff.abs_energy(timeseries)

    leng = len(timeseries)
    app_entropy = tff.approximate_entropy(timeseries, leng, 0.1)

    groups_num = 10
    bin_entropy = tff.binned_entropy(timeseries, 10)

    param_cwt = [{'widths': tuple([2, 2]), 'coef':2, 'w':2}]
    cwt_coef = tff.cwt_coefficients(timeseries, param_cwt)

    param_fft_agg = [{'aggtype': 'skew'}]
    fft_agg = tff.fft_aggregated(timeseries, param_fft_agg)

    param_fft_coef = [{'coef': 2, 'attr': 'angle'}]
    fft_coef = tff.fft_coefficient(timeseries, param_fft_coef)

    abs_soc = tff.absolute_sum_of_changes(timeseries)

    param_agg_acor = [{'f_agg': 'mean', 'maxlag': 2}]
    agg_acor = tff.agg_autocorrelation(timeseries, param_agg_acor)

    param_agg_liner = [{'f_agg': 'mean', 'attr': 'pvalue', 'chunk_len': 2}]
    agg_liner = tff.agg_linear_trend(timeseries, param_agg_liner)

    param_adf = [{'attr': 'pvalue'}]
    adf_test = tff.augmented_dickey_fuller(timeseries, param_adf)

    cid_cd = tff.cid_ce(timeseries, True)

    peak = tff.kurtosis(timeseries)

    mean_absc = tff.mean_abs_change(timeseries)

    mean_sdc = tff.mean_second_derivative_central(timeseries)

    m = 7.8
    ncm = tff.number_crossing_m(timeseries, m)

    features_df = pd.DataFrame()





