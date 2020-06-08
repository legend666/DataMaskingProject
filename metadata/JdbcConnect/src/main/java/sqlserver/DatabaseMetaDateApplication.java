package sqlserver;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.SQLException;


public class DatabaseMetaDateApplication {


    private DatabaseMetaData dbMetaData = null;
    private Connection con = null;


    public DatabaseMetaData getDatabaseMetaData(String diver, String url, String user, String password) {
        try {
            if (dbMetaData == null) {
//                Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
//                String url = "jdbc:sqlserver://localhost:1433;DatabaseName=address_model";
//                String user = "sa";
//                String password = "123456";
                Class.forName(diver);
                con = DriverManager.getConnection(url, user, password);
                dbMetaData = con.getMetaData();
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return dbMetaData;
    }

    //    Python传值到java不知道是什么的时候调用此方法
    public String[] WHATINJAVA(String input) {
        String[] types = {"TABLE"};
        return types;
    }

    public void colseCon() {
        try {
            if (con != null) {
                con.close();
                System.out.println("Connection closed");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

