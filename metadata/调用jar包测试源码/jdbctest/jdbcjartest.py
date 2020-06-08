#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 9:47
# @Author  : legend
import jpype


class GetJarClass(object):
    def start_JVM(self):
        jars = ["D:/JdbcConnect/out/artifacts/JdbcConnect/JdbcConnect.jar"]
        # 获得系统的jvm路径
        jvm_path = jpype.getDefaultJVMPath()
        # jvm参数
        jvm_cp = "-Djava.class.path={}".format(":".join(jars))
        # 启动虚拟机
        jpype.startJVM(jvm_path, jvm_cp)

    def shutdown_JVM(self):
        # 关闭jvm
        jpype.shutdownJVM()

    def shutdown_dbconn(self):
        # 关闭数据库
        jdbc = jpype.JClass("sqlserver.DatabaseMetaDateApplication")
        # 实例化java类
        MetaData = jdbc()
        MetaData.colseCon()

    def MetaData(self, diver, url, user, password):
        jdbc = jpype.JClass("sqlserver.DatabaseMetaDateApplication")
        # 实例化java类
        MetaData = jdbc()
        dbMetaData = MetaData.getDatabaseMetaData(diver, url, user, password)
        return dbMetaData

    # 获取数据库相关信息
    def get_DataBaseInformations(self, dbMetaData):
        print("数据库已知的用户: " + str(dbMetaData.getUserName()))
        print("数据库的系统函数的逗号分隔列表: " + str(dbMetaData.getSystemFunctions()))
        print("数据库的时间和日期函数的逗号分隔列表: " + str(dbMetaData.getTimeDateFunctions()))
        print("数据库的字符串函数的逗号分隔列表: " + str(dbMetaData.getStringFunctions()))
        print("数据库供应商用于 'schema' 的首选术语: " + str(dbMetaData.getSchemaTerm()))
        print("数据库URL: " + str(dbMetaData.getURL()))
        print("是否允许只读:" + str(dbMetaData.isReadOnly()))
        print("数据库的产品名称:" + str(dbMetaData.getDatabaseProductName()))
        print("数据库的版本:" + str(dbMetaData.getDatabaseProductVersion()))
        print("驱动程序的名称:" + str(dbMetaData.getDriverName()))
        print("驱动程序的版本:" + str(dbMetaData.getDriverVersion()))

    # 获得该库下面的所有表
    def get_Tables(self, dbMetaData):
        print('表名----表类型---表备注')
        Resuletset = dbMetaData.getTables(None, None, "%", ('TABLE',))
        while Resuletset.next():
            tableName = Resuletset.getString("TABLE_NAME")
            tableType = Resuletset.getString("TABLE_TYPE")
            remarks = Resuletset.getString("REMARKS")
            print(str(tableName) + '---' + str(tableType) + '---' + str(remarks))

    # 获取该用户下的所有表
    def get_AllViewList(self, dbMetaData):
        types = ('VIEW',)
        print('视图名----视图类型---视图备注')
        resultset = dbMetaData.getTables(None, None, "%", types)
        while resultset.next():
            viewName = resultset.getString("TABLE_NAME")
            viewType = resultset.getString("TABLE_TYPE")
            remarks = resultset.getString("REMARKS")
            print(str(viewName) + "---" + str(viewType) + "---" + str(remarks))

        # 获得表或视图中的所有列信息

    def get_TableColumns(self, dbMetaData, schemaName, table_name):
        print("表目录--表的架构--表名--表中列的索引（从1开始）--列名--"
              "对应的java.sql.Types类型--java.sql.Types类型,名称--列大小--"
              "是否允许为null--列描述--默认值--sql数据类型--char类型的列中的最大字节数--"
              "确定某一列的为空性--是否是自动递增")
        resultset = dbMetaData.getColumns(None, schemaName, table_name, "%")
        while resultset.next():
            tableCat = resultset.getString("TABLE_CAT")
            tableSchemaName = resultset.getString("TABLE_SCHEM")
            tableName_ = resultset.getString("TABLE_NAME")
            columnName = resultset.getString("COLUMN_NAME")
            dataType = resultset.getInt("DATA_TYPE")
            dataTypeName = resultset.getString("TYPE_NAME")
            columnSize = resultset.getInt("COLUMN_SIZE")
            # decimalDigits = resultset.getInt("DECIMAL_DIGITS"); // 小数位数
            # numPrecRadix = resultset.getInt("NUM_PREC_RADIX"); // 基数（通常是10或2）
            nullAble = resultset.getInt("NULLABLE")
            remarks = resultset.getString("REMARKS")
            columnDef = resultset.getString("COLUMN_DEF")
            sqlDataType = resultset.getInt("SQL_DATA_TYPE")
            # sqlDatetimeSub = resultset.getInt("SQL_DATETIME_SUB"); // SQL日期时间分?
            charOctetLength = resultset.getInt("CHAR_OCTET_LENGTH")
            ordinalPosition = resultset.getInt("ORDINAL_POSITION")
            # / **
            # * ISO规则用来确定某一列的为空性。
            # * 是---如果该参数可以包括空值;
            # * 无---如果参数不能包含空值
            # * 空字符串---如果参数为空性是未知的
            # * /
            isNullAble = resultset.getString("IS_NULLABLE")
            #
            # / **
            # * 指示此列是否是自动递增
            # * 是---如果该列是自动递增
            # * 无---如果不是自动递增列
            # * 空字串---如果不能确定它是否
            # * 列是自动递增的参数是未知
            # * /
            isAutoincrement = resultset.getString("IS_AUTOINCREMENT")

            print(str(tableCat) + "--" + str(tableSchemaName) + "--" + str(tableName_) + "--" + str(
                ordinalPosition) + "--" + str(columnName) + "--"
                  + str(dataType) + "--" + str(dataTypeName) + "--" + str(columnSize)
                  + "--" + str(nullAble) + "--" + str(remarks) + "--" + str(columnDef) + "--" + str(sqlDataType) + "--"
                  + str(charOctetLength) + "--" + str(isNullAble) + "--" + str(
                isAutoincrement))

# 获得一个表的索引信息

    def get_IndexInfo(self, dbMetaData, schemaName, tableName):
        print("非唯一索引--索引目录--索引的名称--索引类型--在索引列顺序号--列名--列排序顺序--基数")
        resultset = dbMetaData.getIndexInfo(None, schemaName, tableName, True, True)
        while resultset.next():
            # 非唯一索引(Can index values be non-unique. false when TYPE is  tableIndexStatistic   )
            nonUnique = resultset.getBoolean("NON_UNIQUE")
            # 索引目录（可能为空）
            indexQualifier = resultset.getString("INDEX_QUALIFIER")
            # 索引的名称
            indexName = resultset.getString("INDEX_NAME")
            # 索引类型
            type = resultset.getShort("TYPE")
            # 在索引列顺序号
            ordinalPosition = resultset.getShort("ORDINAL_POSITION")
            # 列名
            columnName = resultset.getString("COLUMN_NAME")
            # 列排序顺序:升序还是降序
            ascOrDesc = resultset.getString("ASC_OR_DESC")
            # 基数
            cardinality = resultset.getInt("CARDINALITY")
            print(str(nonUnique) + "-" + str(indexQualifier) + "-" + str(indexName) + "-" + str(type) + "-" + str(
                ordinalPosition) + "-" + str(columnName) + "-" + str(ascOrDesc) + "-" + str(cardinality))

        # 获得一个表的主键信息

    def get_AllPrimaryKeys(self, dbMetaData, schemaName, tableName):
        print("列名--序列号--主键名称")
        resultset = dbMetaData.getPrimaryKeys(None, schemaName, tableName)
        while resultset.next():
            # 列名
            columnName = resultset.getString("COLUMN_NAME")
            # 序列号(主键内值1表示第一列的主键，值2代表主键内的第二列)
            keySeq = resultset.getShort("KEY_SEQ")
            # 主键名称
            pkName = resultset.getString("PK_NAME")
            print(str(columnName) + "-" + str(keySeq) + "-" + str(pkName))

    # 获得一个表的外键信息
    def getAllExportedKeys(self, dbMetaData, schemaName, tableName):
        print("主键表目录--主键表架构--逐渐表名--主键列名--外键表目录出口--外键表结构出口--外键表名--外键列名--序列号--外键名称--主键名称")
        resultset = dbMetaData.getExportedKeys(None, schemaName, tableName)
        while resultset.next():
            # 主键表的目录（可能为空）
            pkTableCat = resultset.getString("PKTABLE_CAT")
            # 主键表的架构（可能为空）
            pkTableSchem = resultset.getString("PKTABLE_SCHEM")
            # 主键表名
            pkTableName = resultset.getString("PKTABLE_NAME")
            # 主键列名
            pkColumnName = resultset.getString("PKCOLUMN_NAME")
            # 外键的表的目录（可能为空）出口（可能为null）
            fkTableCat = resultset.getString("FKTABLE_CAT")
            # 外键表的架构（可能为空）出口（可能为空）
            fktableschem = resultset.getString("FKTABLE_SCHEM")
            # 外键表名
            fkTableName = resultset.getString("FKTABLE_NAME")
            # 外键列名
            fkColumnName = resultset.getString("FKCOLUMN_NAME")
            # 序列号（外键内值1表示第一列的外键，值2代表在第二列的外键）。
            keySeq = resultset.getShort("KEY_SEQ")

            # updateRule = resultset.getShort("UPDATE_RULE")

            # delRule = resultset.getShort("DELETE_RULE")
            # 外键的名称（可能为空）
            fkName = resultset.getString("FK_NAME")
            # 主键的名称（可能为空）
            pkName = resultset.getString("PK_NAME")
            # deferRability = resultset.getShort("DEFERRABILITY")

            print(str(pkTableCat) + "-" + str(pkTableSchem) + "-" + str(pkTableName) + "-" + str(pkColumnName) + "-"
                  + str(fkTableCat) + "-" + str(fktableschem) + "-" + str(fkTableName) + "-" + str(
                fkColumnName) + "-" + str(keySeq) + "-" + str(fkName) + "-" + str(pkName))


if __name__ == "__main__":
    # 实例化class
    get_class = GetJarClass()
    start_jvm = get_class.start_JVM()
    if jpype.isJVMStarted():
        print("jvm is start")
    # 访问参数
    diver = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    url = "jdbc:sqlserver://localhost:1433;DatabaseName=address_model"
    user = 'sa'
    password = '123456'
    dbMetaData = get_class.MetaData(diver, url, user, password)
    # 获取表
    tables = get_class.get_Tables(dbMetaData)
    # 获取数据库相关信息
    information = get_class.get_DataBaseInformations(dbMetaData)
    # 获得表或视图中的所有列信息
    TableColumns = get_class.get_TableColumns(dbMetaData, None, "行政区划")
    # 获得一个表的索引信息
    info = get_class.get_IndexInfo(None, "行政区划")
    # 获得一个表的主键信息
    primarykey = get_class.get_AllPrimaryKeys(dbMetaData, None, "行区区划")
    # 获得一个表的外键信息
    ExportedKeys = get_class.getAllExportedKeys(dbMetaData, None, '楼房地址数据')
    # 关闭数据库连接
    get_class.shutdown_dbconn()
    shutdown_jvm = get_class.shutdown_JVM()
