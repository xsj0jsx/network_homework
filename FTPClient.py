#!/usr/bin/python

from ftplib import FTP
import ftplib
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('-ip',default='127.0.1.1')
parser.add_argument('-list')
parser.add_argument('-download', nargs=2)
parser.add_argument('-upload', nargs=2)

args = parser.parse_args()
ftp = FTP()
ftp.connect(args.ip, 8888)
def enterRemotePath(p):
    dstp = os.path.dirname(p)
    try:
        ftp.cwd(dstp)
    except ftplib.error_perm:
        print 'ERRORL cannot CD to "%s"' % dstp
        f.quit()
        exit()
    print '*** Changed to "%s" folder' % dstp
    
def download(data):
    f = open(localName, 'wb')
    try:
        f.write(data)
    finally:
        f.close()
if args.list:
    listDir = args.list
    enterRemotePath(listDir)
    ftp.dir()
elif args.download:
    remotePath, localName = args.download
    remoteName = os.path.basename(remotePath)
    enterRemotePath(remotePath)
    try:
        ftp.retrbinary('RETR %s' % remoteName, download)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % remoteName
    else:
        print '*** Downloaded "%s" to "%s"' % (remoteName, localName)
elif args.upload:
    localName, remotePath = args.upload
    remoteName = os.path.basename(remotePath)
    enterRemotePath(remotePath)
    try:
        f = open(localName,'r')
        ftp.storbinary('STOR %s' % remoteName, f)
    except ftplib.error_perm:
        print 'ERROR: cannot write file "%s"' % remoteName
    except IOError as err:
        print "File Error:", str(err)
    else:
        print '*** Upload "%s" to "%s"' % (localName, remoteName)
ftp.quit()
ftp.close()
    
