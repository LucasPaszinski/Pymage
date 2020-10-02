from concurrent.futures.process import ProcessPoolExecutor
import multiprocessing as multi
import pyautogui as auto


def _p_finder(image, region, sender):
    try:
        res = auto.locateOnScreen(
            image,
            region=region,
            grayscale=True,
            confidence=0.8)
        if res != None:
            try:
                # exception might be raised because connection is closed
                sender.send(res)
                sender.close()
            except:
                pass
            AddHitFor(image)
            # print(f'*** The Image {image} was Found ***\t\t\t\t')
    except:
        return [True, None]


def _start_parallel_image_search(images, region, max_cores_threads=6):
    awaiting = []  # list of processes created
    started = []
    receiver, sender = multi.Pipe(False)
    for image in images:
        p = multi.Process(target=_p_finder, args=(image, region, sender,))

        if started.__len__() < max_cores_threads:
            started.append(p)
            p.start()
        else:
            awaiting.append(p)

    return started, awaiting, receiver


def _queue_manage_await_response(started, awaiting, receiver):
    for process in started:
        process.join()

        if(receiver.poll()):
            result = receiver.recv()
            if result != None:
                receiver.close()
                return result

        if awaiting.__len__() > 0:
            a_process = awaiting.pop(0)
            a_process.start()
            started.append(a_process)

    return None


def _finish_processes(list_of_process):
    for process in list_of_process:
        try:
            process.close()
            process.terminate()
            process.kill()
        except:
            pass


def parallel_finder(images, region, max_cores_threads=4):
    try:
        started, awaiting, receiver = _start_parallel_image_search(
            images, region, max_cores_threads)
        result = _queue_manage_await_response(started, awaiting, receiver)
        _finish_processes(started + awaiting)
        return result
    except:
        return [True, None]


def _p_locateAll(image):
    try:
        results = []
        locateAll_result = auto.locateAllOnScreen(image)

        for res in locateAll_result:
            results.append(res)

        return results
    except:
        return None


def parallel_findall(images, max_cores_threads=4):
    try:
        result_of_locateAll = []
        with ProcessPoolExecutor(max_workers=max_cores_threads) as ppe:
            for image in images:
                result = ppe.submit(_p_locateAll, image)
                result_of_locateAll.append(result)

        filtered_result = []
        for result in result_of_locateAll:
            r = result.result()
            if r != []:
                filtered_result = filtered_result + r

        return list(filtered_result)

    except:
        return list()

def AddHitFor(image):
    '''Write on a image frequency file onde a image is found'''
    if not (str.isspace(image) or image == None):
        image_freq_list = open('codegenerator/image_frequency_list.txt',"a")
        image_freq_list.write(image+"\n")
        image_freq_list.close()
