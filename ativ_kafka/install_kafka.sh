yum install -y java
wget https://downloads.apache.org/kafka/3.6.0/kafka_2.12-3.6.0.tgz
tar -xvf kafka_2.12-3.6.0.tgz
mv kafka_2.12-3.6.0 /opt
useradd kafka
chown -R kafka:kafka /opt/kafka_2.12-3.6.0
printf '[Unit]\nDescription=zookeeper\nAfter=syslog.target network.target\n[Service]\nType=simple\nUser=kafka\nGroup=kafka\nExecStart=/opt/kafka_2.12-3.6.0/bin/zookeeper-server-start.sh /opt/kafka_2.12-3.6.0/config/zookeeper.properties\nExecStop=/opt/kafka_2.12-3.6.0/bin/zookeeper-server-stop.sh\n[Install]\nWantedBy=multi-user.target' > /etc/systemd/system/zookeeper.service
printf '[Unit]\nDescription=Apache Kafka\nRequires=zookeeper.service\nAfter=zookeeper.service\n[Service]\nType=simple\nUser=kafka\nGroup=kafka\nExecStart=/opt/kafka_2.12-3.6.0/bin/kafka-server-start.sh /opt/kafka_2.12-3.6.0/config/server.properties\nExecStop=/opt/kafka_2.12-3.6.0/bin/kafka-server-stop.sh\n[Install]\nWantedBy=multi-user.target' >  /etc/systemd/system/kafka.service
sed -i '/export KAFKA_HEAP_OPTS="-Xmx1G -Xms1G"/c\export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"' /opt/kafka_2.12-3.6.0/bin/kafka-server-start.sh

# kafka server config
sed -i '/broker.id=0/c\broker.id=1' /opt/kafka_2.12-3.6.0/config/server.properties
sed -i '/zookeeper.connect=localhost:2181/c\zookeeper.connect=172.31.24.134:2181' /opt/kafka_2.12-3.6.0/config/server.properties
printf 'inter.broker.listener.name=INTERNAL\nlistener.security.protocol.map=INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT\nlisteners=INTERNAL://0.0.0.0:19092,EXTERNAL://0.0.0.0:9092\nadvertised.listeners=INTERNAL://172.31.24.87:19092,EXTERNAL://34.236.153.230:9092' >> /opt/kafka_2.12-3.6.0/config/server.properties

systemctl start zookeeper
systemctl start kafka
