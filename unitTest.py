#!/usr/bin/python
import unittest
import server
class MockConnection:
    def send(self,msg):
        self.msg = msg
    def close(self):
        pass
    def recv(self,size):
        return ""
class TestFTPserverThread(unittest.TestCase):
    def setUp(self):
        self.conn = MockConnection()
        self.ftp = server.FTPserverThread( (self.conn, "1.1.1.1") )
    def test_QUIT(self):
        self.ftp.QUIT("")
        self.assertEqual(self.conn.msg, "221 Goodbye.\r\n")
    def test_SYST(self):
        self.ftp.SYST("")
        self.assertEqual(self.conn.msg, "215 UNIX Type: L8\r\n")
class TestHTTPserverThread(unittest.TestCase):
    def setUp(self):
        self.conn = MockConnection()
        self.http = server.HTTPserverThread( (self.conn, "1.1.1.1") )
    def test_run(self):
        self.http.run()
        self.assertEqual(self.conn.msg, "hello")
if __name__ == '__main__':
    unittest.main()
