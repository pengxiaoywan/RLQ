from algorithm import Algorithm
from analysis import Analysis


if __name__ == '__main__':

    tool = Analysis('results_algorithm/')
    name = 'MC'
    algorithm = Algorithm(name)
    runtime = algorithm.execute(network_path='networks/',
                                sub_filename='sub-wm.txt',
                                req_num=1000)
    tool.save_evaluations(algorithm.evaluation, '%s.txt' % name)
    print(runtime)
# 9321 ts
# 8974 wm