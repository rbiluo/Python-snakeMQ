# -*-coding:utf-8 -*-
def main():
    def on_recv(conn, ident, message):
        if message.data == 'do':
            print 'I can do it...'
            time.sleep(5)
            tmp_msg = 'do'
            msg = snakemq.message.Message(tmp_msg,ttl=600)
            messaging.send_message(ident, msg)
        if message.data != 'do':
            print 'Get a task'
            time.sleep(5)
            line = message.data
            print line
            print 'Hello, World!'
            tmp_msg = 'done'
            msg = snakemq.message.Message(tmp_msg,ttl=600)
            messaging.send_message(ident, msg)
        
    def on_connect(conn, ident):
        print "%s is connect" % ident
        time.sleep(5)
        tmp_msg = "hi,server, i am cient"
        msg = snakemq.message.Message(tmp_msg,ttl=600)
        messaging.send_message(ident, msg)

    def on_disconnect(conn, ident):
        print "%s is disconnect." % ident
        time.sleep(5)

    snakemq_ip = "localhost"
    snakemq_port = 6001
    link = snakemq.link.Link()
    link.add_connector((snakemq_ip, snakemq_port))
    packeter = snakemq.packeter.Packeter(link)
    messaging = snakemq.messaging.Messaging("client","",packeter)
    
    messaging.on_message_recv= on_recv
    messaging.on_connect = on_connect
    messaging.on_disconnect = on_disconnect

    link.loop()
    link.cleanup()
    

if __name__ == "__main__":
    import time
    import snakemq
    import snakemq.link
    import snakemq.packeter
    import snakemq.messaging
    import snakemq.message
    main()
