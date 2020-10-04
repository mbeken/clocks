package com.schlumberger.clock.config

import java.io.{FileNotFoundException, InputStream}
import java.util.Properties

import scala.io.Source
import scala.reflect.internal.util.NoSourceFile.path


/**
 * @author Piyush
 * Utility class to read data from property file
 */
object ReadConfig {

  val prop = new Properties
  val propFileName = "F:/schlumberg/clocks/src/config/config.properties"

//  val inputStream: InputStream = getClass.getClassLoader.getResourceAsStream(propFileName)
//  prop.load(inputStream)

  def getConfig(key: String): String = {
    import java.io.FileInputStream
    val properties = new Properties()
    val in = new FileInputStream("F:/schlumberg/clocks/src/config/config.properties")
    properties.load(in)

    properties.getProperty(key)

  }
}
