import copy
import networkx as nx

def main():
    err = 0
    processes = 4
    resources = 4
    max_resources = [1, 1, 1, 1]
    label = 'Безопасная последовательность:'
    sequence = ""
    lst_of_sec = []

    print("\n-- maximum resources for each process --")
    max_need = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    print("\n-- allocated resources for each process --")
    currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]


    print("\n-- request resources for each process --")
    currently_request = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    allocated = [0] * resources
    for i in range(processes):
        for j in range(resources):
            allocated[j] += currently_allocated[i][j]
    available = [max_resources[i] - allocated[i] for i in range(resources)]

    bankir(err, processes, resources, max_resources, max_need, currently_allocated, currently_request, available, allocated, sequence, label, lst_of_sec)


def bankir(err, processes, resources, max_resources, max_need, currently_allocated, currently_request, available, allocated, sequence, label, lst_of_sec):
    rest = 1
    draw_req = []
    draw_all = []
    lst_of_sec = []
    draw_req.append(copy.deepcopy(currently_request))
    draw_all.append(copy.deepcopy(currently_allocated))
    if_not_safe1 = copy.deepcopy(currently_allocated)
    if_not_safe2 = copy.deepcopy(currently_request)
    if_not_safe3 = copy.deepcopy(max_need)
    if_not_safe2_prev = copy.deepcopy(currently_request)
    trans_matrix = list(zip(*if_not_safe1))
    if_not_safe1 = copy.copy([list(row) for row in trans_matrix])

    null_lst = []
    running = [True] * processes
    safe = False
    count = 4
    flag = 1
    for i in range(processes):
        if flag:
            for j in range(resources):
                if currently_request[i][j] > max_need[i][j]:
                    count = 0
                    err = i
                    flag = 0
        else:
            break
    while count != 0:
        for i in range(4):
            if running[i]:
                executing = True
                for j in range(resources):
                    if currently_request[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing: # выделение ресурсов и запуск проверки
                    available1 = copy.copy(available)
                    currently_allocated1 = copy.copy(currently_allocated)
                    currently_request1 = copy.copy(currently_request)
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    for j in range(resources):
                        currently_allocated[i][j] = 0
                    for j in range(resources):
                        currently_request[i][j] = 0
                    draw_req.append(copy.deepcopy(currently_request))
                    draw_all.append(copy.deepcopy(currently_allocated))
                    # проверка на безопасность
                    work = copy.copy(available)
                    finish = [0]*processes
                    is_end = True
                    sign_not_safe = 0
                    while is_end:
                        for j in range(resources):
                            if sign_not_safe == 2: #currently_request[finish.index(0)][j] > work[j] and finish.count(0) == 1:
                                is_end = False
                                break

                        for k in range(processes):
                            is_ok = True
                            for j in range(resources):
                                if currently_request[k][j] > work[j]:
                                    is_ok = False
                                    break
                            if is_ok:
                                finish[k] = 1
                                if sign_not_safe == 0:
                                    for j in range(resources):
                                        work[j] += currently_allocated[k][j]
                        sign_not_safe += 1

                    if 0 in finish:
                        draw_req.append(copy.deepcopy(currently_request))
                        draw_all.append(copy.deepcopy(currently_allocated))
                        #count = 0
                        currently_request = currently_request1
                        currently_allocated = currently_allocated1
                        available = available1
                        print(f"Запрос процесса {i + 1} не выполнен, система не в безопасном состоянии\n")
                    else:
                        rest += 1
                        null_lst.append(i)
                        count -= 1
                        # available[i] += 1
                        # for n in range(4):
                        #     currently_allocated[i][n] -= currently_request[i][n]
                        #     currently_request[i][n] == 0

                        print(f"Процесс {i + 1} выполнен")
                        lst_of_sec.append(i + 1)
                        print("выделено ресурсов:")
                        [print(*currently_allocated[i]) for i in range(4)]
                        print("запрос на ресурсы:")
                        [print(*currently_request[i]) for i in range(4)]

                        if count:
                            sequence += f"{i + 1} -> "
                        else:
                            sequence += f"{i + 1}"
                        running[i] = False
                        safe = True
                        break
        if not safe:
            label = "Система в небезопасном состоянии\n"
            print(label)
            #print(draw_all)
            #print(draw_req)
            draw_req = [if_not_safe2]
            draw_all = [if_not_safe1]
            #print(len(draw_all))
            #print(draw_all)
            rest = 1
            # # transponir
            #trans_matrix = list(zip(*draw_all))
            #draw_all = copy.copy(list(row) for row in trans_matrix)
            print(draw_all)

            adj_matrix = {
                'R1': [],
                'R2': [],
                'R3': [],
                'R4': [],
                'P1': [],
                'P2': [],
                'P3': [],
                'P4': []
            }
            for proc in range(4):
                for x in range(4):
                    if draw_all[0][proc][x] == 1:
                        adj_matrix[f'R{proc + 1}'].append(f'P{x + 1}')
                    if draw_req[0][proc][x] == 1:
                        adj_matrix[f'P{proc + 1}'].append(f'R{x + 1}')

            # удаляем ключи
            to_remove = [key for key, value in adj_matrix.items() if value == []]
            for key in to_remove:
                del adj_matrix[key]
            print(adj_matrix)

            graph = nx.DiGraph(adj_matrix)

            cycles = nx.simple_cycles(graph)
            cyc = []

            # ['P2', 'R1', 'P1', 'R3']
            for cycle in cycles:
                cyc += cycle

            #[['P2', 'R1'], ['R1', 'P1'], ['P1', 'R3'], ['R3', 'P2']]

            if cyc:
                cyc.append(cyc[0])
                cycle_res = [[cyc[i], cyc[i+1]] for i in range(len(cyc)-1)]
            else:
                cycle_res = []

            for cycl in range(len(cycle_res)):
                for i in range(4):
                    if f'R{i + 1}' in cycle_res[cycl][0]:
                        for j in range(4):
                            if f'P{j + 1}' in cycle_res[cycl][1]:
                                draw_all[0][i][j] = -1
                    if f'P{i + 1}' in cycle_res[cycl][0]:
                        for k in range(4):
                            if f'R{k + 1}' in cycle_res[cycl][1]:
                                draw_req[0][i][k] = -1
            #print(draw_req)
            return err, if_not_safe1, if_not_safe2_prev, if_not_safe3, null_lst, label, sequence, draw_req, draw_all, rest, lst_of_sec

    if safe:
        # transponir
        transposed_matrix_list = []

        for matrix in draw_all:
            transposed_matrix = []
            for i in range(len(matrix[0])):
                transposed_row = []
                for row in matrix:
                    transposed_row.append(row[i])
                transposed_matrix.append(transposed_row)
            transposed_matrix_list.append(transposed_matrix)
        draw_all = copy.copy(transposed_matrix_list)

        rest = 5
        #print(lst_of_sec)
        return err, if_not_safe1, if_not_safe2_prev, if_not_safe3, null_lst, label, sequence, draw_req, draw_all, rest, lst_of_sec
    else:
        label = "Ошибка:\n"
        sequence = f"Процесс {err + 1} превысил максимальную\nпотребность!"
        print(label)
        rest = 0
        return err + 1, if_not_safe1, if_not_safe2_prev, if_not_safe3, null_lst, label, sequence, draw_req, draw_all, rest, lst_of_sec
if __name__ == "__main__":
    main()
