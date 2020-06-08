1.获取所有用户名:
SELECT name FROM Sysusers where status='2' and islogin='1'
islogin='1'表示帐户
islogin='0'表示角色
status='2'表示用户帐户
status='0'表示糸统帐户


2.获取所有数据库名:
SELECT Name FROM Master..SysDatabases ORDER BY Name


3.获取所有表名
SELECT Name FROM DatabaseName..SysObjects Where XType='U' ORDER BY Name
XType='U':表示所有用户表;
XType='S':表示所有系统表;


4.获取所有字段名:
SELECT Name FROM SysColumns WHERE id=Object_Id('TableName')


5.获取数据库所有类型
select name from systypes


6.获取主键字段
SELECT name FROM SysColumns WHERE id=Object_Id('表名') and colid=(select top 1 keyno from sysindexkeys where id=Object_Id('表名'))

 

7、获取字段类型

select a.name as [column],b.name as type from syscolumns a,systypes b where a.id=object_id('表名') and a.xtype=b.xtype

或者可以通过存储过程 exec sp_help 表名

 

8、取表结构

select column_name,data_type,character_maximum_length from information_schema.columns where table_name = '表名'


Select  
  字段名=rtrim(b.name),  
  主键=CASE WHEN h.id IS NOT NULL  THEN 'PK' ELSE '' END,  
  字段类型=type_name(b.xusertype)+CASE WHEN b.colstat&1=1 THEN '[ID(' + CONVERT(varchar, ident_seed(a.name))+','+CONVERT(varchar,ident_incr(a.name))+')]' ELSE '' END,  
  长度=b.length,   
  允许空=CASE b.isnullable WHEN 0 THEN 'N' ELSE 'Y' END,   
  默认值=isnull(e.text, ''),  
  字段说明=isnull(c.value, '')  
FROM sysobjects a, syscolumns b  
LEFT OUTER JOIN sys.extended_properties c ON b.id = c.major_id AND b.colid = c.minor_id
LEFT OUTER JOIN syscomments e ON b.cdefault = e.id  
LEFT OUTER JOIN (Select g.id, g.colid FROM sysindexes f, sysindexkeys g Where (f.id=g.id)AND(f.indid=g.indid)AND(f.indid>0)AND(f.indid<255)AND(f.status&2048)<>0) h ON (b.id=h.id)AND(b.colid=h.colid)  
Where (a.id=b.id)AND(a.id=object_id('要查询的表'))  --要查询的表改成你要查询表的名称 
orDER BY b.colid
Select  
  表名=case when a.colorder=1 then d.name else '' end,  
  表说明=case when a.colorder=1 then isnull(f.value,'') else '' end,  
  字段序号=a.colorder,  
  字段名=a.name,  
  标识=case when COLUMNPROPERTY(a.id,a.name,'IsIdentity')=1 then '√' else '' end,  
  主键=case when exists(Select 1 FROM sysobjects where xtype='PK' and name in (Select name FROM sysindexes Where indid in(Select indid FROM sysindexkeys Where id=a.id AND colid=a.colid))) then '√' else '' end,     
  类型=b.name,  
  字段长度=a.length,  
  占用字节数=COLUMNPROPERTY(a.id,a.name,'PRECISION'),  
  小数位数=isnull(COLUMNPROPERTY(a.id,a.name,'Scale'),0),  
  允许空=case when a.isnullable=1 then '√'else '' end,  
  默认值=isnull(e.text,''),  
  字段说明=isnull(g.[value],'')  
FROM syscolumns a  
left join systypes b on a.xusertype=b.xusertype  
inner join sysobjects d on (a.id=d.id)and(d.xtype='U')and(d.name<>'dtproperties')  
left join syscomments e on a.cdefault=e.id  
left join sys.extended_properties g on (a.id=g.major_id)and(a.colid=g.minor_id)  
left join sys.extended_properties f on (d.id=f.major_id)and(f.minor_id=0)  
--where d.name='要查询的表'         --如果只查询指定表,加上此条件 
order by a.id,a.colorder  
