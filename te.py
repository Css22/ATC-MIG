from util.sharing import *
from node.GPU_worker import woker
import node.GPU_worker as GPU_worker
import node.Scheduler_worker as Scheduler_worker
import util.MIG_operator as MIG_operator
import random
import time
import os
import signal
job_list = get_job_list()
random.seed(17)
def offline_job_generator(num):
    
    # job_list = ["GAN","transformer","bert","resnet50","resnet152","mobilenet","deeplabv3","SqueezeNet","unet","vit"]
    job_list = ["GAN","resnet50","bert"]
    epoch_num = [100,200,300]
    offline_job_list = []
    for i in range(0, num):
        # random_ID = random.randint(1, 1000000)
        random_model = random.choice(job_list)
        random_epoch = random.choice(epoch_num)
        random_epoch = random_epoch
        offline_job_list.append(offline_job(random_model, batch_Size=None, epoch=random_epoch))
    return offline_job_list

def online_job_generator(num):
    global job_list
    online_job_list = []
    # job_name_list = ['alexnet', 'bert', 'deeplabv3', 'inception_v3', 'mobilenet_v2', 'resnet50', 'resnet101', 'resnet152', 'unet', 'vgg16', 'vgg19']
    job_name_list  = ["bert","resnet152","resnet50","vgg19","mobilenet_v2"]
    base_size_list = [32]
    config_map = {7:"1c-7g-80gb", 4:"1c-4g-40gb", 3:"1c-3g-40gb", 2:"1c-2g-20gb", 1:"1c-1g-10gb"}
    node1 =  woker()
    for i in range(0, num):
        qos = [40,50,60,70,80,90,100,110,120,130,140,150,160,170]
       
        while True:
            random_batch = random.choice(base_size_list)
            random_model = random.choice(job_name_list)
            random_qos = random.choice(qos)

            flag = False
            online_job_item = online_job(model_name=random_model, batch_Size=random_batch, qos=random_qos)
            if node1.best_fit(online_job=online_job_item) != 100:
                config_id = node1.best_fit(online_job=online_job_item)
                config  = config_map.get(config_id)

                for j in job_list:
                    if j.batch_Size == None :
                        continue
             
                    if j.model_name == online_job_item.model_name and int(j.batch_Size)== int(online_job_item.batch_Size) and j.config == config:
                        if float(j.average_time) * 1000/online_job_item.qos < 0.7:
                            online_job_list.append(online_job_item)
                            flag = True
                            break
                        else:
                            break
         
            if flag:
                break  
                            
    return online_job_list

offline_jobs = offline_job_generator(4)
online_jobs = online_job_generator(2)


jobs = []
for i in online_jobs:
    jobs.append(i)

for i in offline_jobs:
    jobs.append(i)
GPU_worker.regist_worker()

node1 = woker()
node1.cluster_algorithm = 'me'
GPU_worker.WorkerService()
# MIG_operator.reset_mig(0)

# generate_jobid(jobs)
# jobs = generate_jobs()
# jobs[4].epoch = 4

# node1.start_update_load()



jobs1  = []
test_job1 = online_job(model_name='bert', batch_Size=32, qos=200)



# jobs1.append(jobs[0])

# jobs1.append(jobs[1])
# jobs1.append(jobs[2])
jobs1.append(test_job1)
jobs1.append(jobs[3])

for i in jobs1:
    
    print(i)


print(node1.partition_optimizer(jobs=jobs1, GPU_index=0))
print(node1.GPU_list)
# print(jobs[3].model_name)

# print(node1.config_list, node1.GPU_list)
# print(jobs[3].gi_id)





# node1.node_schedule(new_job=jobs[0], gpu_id=0)
# print(node1.GPU_list, node1.config_list)

# time.sleep(20)
# node1.node_schedule(new_job=jobs[1], gpu_id=0)
# print(node1.GPU_list, node1.config_list)

# time.sleep(20)
# node1.node_schedule(new_job=jobs[2], gpu_id=0)
# print(node1.GPU_list, node1.config_list)
# print(jobs[2].gi_id)

# time.sleep(20)
# node1.node_schedule(new_job=jobs[3], gpu_id=0)
# print(node1.GPU_list, node1.config_list)
# print(jobs[3].gi_id)

# print(node1.node_schedule(new_job=jobs[3], gpu_id=0))
# print(node1.node_schedule(new_job=jobs[4], gpu_id=0))



# while True:
#     time.sleep(1)
#     print(GPU_worker.busy_table, node1.GPU_list[0], node1.config_list[0])
# jobs[3].epoch = 10
# node1.executor(job=jobs[0], UUID='MIG-2428a716-ba1a-5eae-959f-22f6c93b0f14')
# node1.executor(job=jobs[3], UUID='MIG-b9073a99-3746-564b-bb04-f5f719f2771c')
# time.sleep(600)
# print(node1.jobs_pid)
# os.kill(node1.jobs_pid[jobs[0].jobid], signal.SIGTERM) 
# os.kill(node1.jobs_pid[jobs[3].jobid], signal.SIGTERM) 


# generate_job_progress_table(jobs)


# print(read_job_progress(0))
# record_job_progress(0, 11)
# print(read_job_progress(0))
# node1.node_schedule(jobs[0], 0)
# print(node1.config_list)
# print(node1.GPU_list)
# print(node1.throughput)
# print(GPU_worker.UUID_table)

# time.sleep(2)

# node1.node_schedule(jobs[1], 0)
# print(node1.config_list)
# print(node1.GPU_list)
# print(node1.throughput)
# print(GPU_worker.UUID_table)


# time.sleep(2)
# node1.node_schedule(jobs[2], 0)
# print(node1.config_list)
# print(node1.GPU_list)
# print(node1.throughput)
# print(GPU_worker.UUID_table)

# time.sleep(2)
# print(node1.node_schedule(jobs[3], 0))
# print(node1.config_list)
# print(node1.GPU_list)
# print(node1.throughput)
# print(GPU_worker.UUID_table)