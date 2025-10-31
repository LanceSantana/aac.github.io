import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import { GoogleGenerativeAI } from "@google/generative-ai";

// Load environment variables
dotenv.config();

const app = express();
app.use(express.json());
app.use(cors());

// Initialize Gemini client
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

// --- TEST ROUTE ---
app.get("/", (req, res) => {
  res.send("✅ Gemini API backend is running!");
});

// --- GEMINI ROUTE ---
app.post("/api/gemini", async (req, res) => {
  try {
    const { text } = req.body;

    if (!text || text.trim() === "") {
      return res.status(400).json({ error: "No input text provided" });
    }

    const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });

    const result = await model.generateContent(text);
    const reply = result.response.text();

    console.log("Gemini Reply:", reply);
    res.json({ reply });
  } catch (err) {
    console.error("❌ Gemini Error:", err);
    res.status(500).json({ error: "Gemini API request failed" });
  }
});

// --- START SERVER ---
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🚀 Server running on http://localhost:${PORT}`));
