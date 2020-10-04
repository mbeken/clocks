package com.schlumberger.clock.utils

import java.sql._

import com.schlumberger.clock.config.ReadConfig
import org.apache.spark.sql.ForeachWriter

class JDBCSink(url: String, user: String, password: String) extends org.apache.spark.sql.ForeachWriter[org.apache.spark.sql.Row] {

  var driver = "com.mysql.jdbc.Driver"
  var connection: Connection = _
  var statement: Statement = _

  override def open(partitionId: Long, version: Long): Boolean = {
    Class.forName(driver)
    connection = DriverManager.getConnection(url, user, password)
    statement = connection.createStatement()
    true
  }

  override def process(value: org.apache.spark.sql.Row): Unit = {
    val database = "test"
    val table = "clock"
    println("value 0 ---->> " + value(0).toString + " ---- value 1 " + value(1).toString)
    val stmt = "INSERT into " + table + " VALUES (" + "'" + value(0).toString + "'" + "," + "'" + value(1).toString + "'" + ");"
    println("statement : " + stmt)
    statement.execute(stmt)
  }

  override def close(errorOrNull: Throwable): Unit = {
    connection.close()
  }

}
