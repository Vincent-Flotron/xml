using System;
using System.Xml;
using System.Xml.Xsl;

public class XmlTransformer
{
    public void TransformXml(string xmlFilePath, string xslFilePath, string outputFilePath)
    {
        // Load the XML and XSL files
        XmlDocument xmlDoc = new XmlDocument();
        xmlDoc.Load(xmlFilePath);

        XslCompiledTransform xslt = new XslCompiledTransform();
        xslt.Load(xslFilePath);

        // Perform the transformation
        XmlWriterSettings settings = new XmlWriterSettings
        {
            Indent = true,
            IndentChars = "  " // Set the desired indentation character(s)
        };

        using (XmlWriter writer = XmlWriter.Create(outputFilePath, settings))
        {
            xslt.Transform(xmlDoc, null, writer);
        }
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        // Check the number of command-line arguments
        if (args.Length < 3)
        {
            Console.WriteLine("Insufficient arguments.");
            Console.WriteLine("Usage: program.exe xmlFilePath xslFilePath outputFilePath");
            return;
        }

        string xmlFilePath = args[0];
        string xslFilePath = args[1];
        string outputFilePath = args[2];

        // Create an instance of XmlTransformer and perform the transformation
        XmlTransformer transformer = new XmlTransformer();
        transformer.TransformXml(xmlFilePath, xslFilePath, outputFilePath);

        Console.WriteLine("Transformation complete.");
    }
}
