import happybase

# get connect
connet=happybase.Connection(host='192.168.56.191', port=9090)
# create table
connet.create_table('qstest:zf_test_py',{'f1':dict(max_version=3),'f2':dict() ,'f3':dict()})
# drop table
connet.delete_table(name='qstest:zf_test_py',disable=True)
# get table object
table=connet.table(name='qstest:zf_test_py')
# get columnfamily info  from table
families=table.families()
# get region info from table
reginInfo =table.regions()
# put data into table
table.put('A1',{'f1:addr':"addr1",'f2:name':'name1'},timestamp=1,wal=True)
table.put('A2',{'f1:addr':"addr2",'f2:name':'name2'},timestamp=1,wal=True)
table.put('A3',{'f1:addr':"addr3",'f2:name':'name3'},timestamp=1,wal=True)

# put dateList into table
with table.batch(batch_size=100) as putList:
    for i in range(4,10):
        putList.put('A%s' % i,{'f1:addr':"addr%s" % i,'f2:name':'name%s' % i},timestamp=i,wal=True)

#scan table
scanList=table.scan(row_start='A1',row_stop='A9',columns='f1:addr',batch_size=5,limit=10,scan_batching=True)

# get row from table
row1 =table.row(row='A1',columns=['f1:name','f2:addr'])
rowList =table.row(row=['A1','A2'],columns=['f1:name','f2:addr'])
#get cell from table
cell1=table.cells(row='A1',column='f1:addr',include_timestamp=True)
cell2=table.cells(row='A1',column='f1:addr',versions=1,timestamp=1,include_timestamp=False)
#del date from table
table.delete(row='A1',columns='f1:addr',timestamp='1',wal=True)



