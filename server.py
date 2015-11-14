# -*-coding:utf-8 -*-
def main():
    task = "Please Print 'hello, world!'"
    def on_recv(conn, ident, message):
        if message.data != 'do':
            print 'waiting...'
            time.sleep(5)
        if message.data == 'do':
            tmp_msg = task
            msg = snakemq.message.Message(tmp_msg, ttl=600)
            messaging.send_message(ident, msg)
        if message.data == 'done':
            print 'success!!!'
            time.sleep(5)

    def on_connect(conn, ident):
        print "%s is connect" % ident
        time.sleep(5)
        tmp_msg = "do"
        msg = snakemq.message.Message(tmp_msg,ttl=600)
        messaging.send_message(ident,msg)

    def on_disconnect(conn, ident):
        print "%s is disconnect." % ident
        time.sleep(5)

    snakemq_ip = "localhost"
    snakemq_port = 6001
    link = snakemq.link.Link()
    link.add_listener((snakemq_ip, snakemq_port))
    packeter = snakemq.packeter.Packeter(link)
    messaging = snakemq.messaging.Messaging("server","",packeter)

    messaging.on_message_recv.add(on_recv)
    messaging.on_connect = on_connect
    messaging.on_disconnect = on_disconnect

    link.loop()
    link.cleanup()


if __name__ == "__main__":
    import snakemq
    import snakemq.link
    import snakemq.packeter
    import snakemq.messaging
    import snakemq.message  
    import time
    main()
    
    
