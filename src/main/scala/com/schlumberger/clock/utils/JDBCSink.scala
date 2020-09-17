package com.schlumberger.clock.utils

import org.apache.spark.sql.ForeachWriter
import java.sql._

import com.schlumberger.clock.config.ReadConfig

class JDBCSink(url: String, user: String, password: String) extends ForeachWriter[(String, String)] {

  var driver = ReadConfig.getConfig("driver")
  var connection: Connection = _
  var statement: Statement = _

  override def open(partitionId: Long, version: Long): Boolean = {
    Class.forName(driver)
    connection = DriverManager.getConnection(url, user, password)
    statement = connection.createStatement()
    true
  }

  override def process(value: (String, String)): Unit = {
    val database = ReadConfig.getConfig("database")
    val table = ReadConfig.getConfig("table")
    statement.execute("INSERT into " + database + "." + table + " VALUES (" + value._1 + "," + value._2 + ")")
  }

  override def close(errorOrNull: Throwable): Unit = {
    connection.close()
  }
}
