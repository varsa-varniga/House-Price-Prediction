import React, { useState } from "react";
import axios from "axios";
import {
  TextField,
  Button,
  Typography,
  Box,
  Container,
  Paper,
  CircularProgress,
} from "@mui/material";
import { motion as _motion } from "framer-motion";
import HomeIcon from "@mui/icons-material/Home";
import "./App.css";

function App() {
  const [area, setArea] = useState("");
  const [bedrooms, setBedrooms] = useState("");
  const [location, setLocation] = useState("");
  const [predictedPrice, setPredictedPrice] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handlePredict = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setPredictedPrice(null);

    try {
      const response = await axios.post("http://localhost:5000/predict", {
        area: Number(area),
        bhk: Number(bedrooms),
        location: location,
      });

      setPredictedPrice(response.data.predicted_price);
    } catch (error) {
      console.error("Error making prediction:", error);
      setError("Prediction failed. Please check your inputs or server.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <Container maxWidth="sm">
        <_motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <Paper
            elevation={4}
            sx={{
              padding: 4,
              borderRadius: "20px",
              backdropFilter: "blur(12px)",
              backgroundColor: "rgba(255, 255, 255, 0.7)",
              boxShadow: "0px 8px 20px rgba(0,0,0,0.2)",
              mt: 5,
            }}
          >
            <Typography
              variant="h4"
              align="center"
              gutterBottom
              color="primary"
              fontWeight={"bold"}
              display="flex"
              justifyContent="center"
              alignItems="center"
              gap={1}
            >
              <HomeIcon /> House Price Prediction
            </Typography>

            <form onSubmit={handlePredict}>
              <Box mb={2}>
                <TextField
                  label="Area (sq. ft.)"
                  type="number"
                  variant="outlined"
                  fullWidth
                  value={area}
                  onChange={(e) => setArea(e.target.value)}
                  required
                />
              </Box>
              <Box mb={2}>
                <TextField
                  label="Number of Bedrooms"
                  type="number"
                  variant="outlined"
                  fullWidth
                  value={bedrooms}
                  onChange={(e) => setBedrooms(e.target.value)}
                  required
                />
              </Box>
              <Box mb={2}>
                <TextField
                  label="Location"
                  variant="outlined"
                  fullWidth
                  value={location}
                  onChange={(e) => setLocation(e.target.value)}
                  required
                />
              </Box>
              <Box mt={2} display="flex" justifyContent="center">
                <_motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
                  <Button
                    variant="contained"
                    color="primary"
                    type="submit"
                    disabled={loading}
                    sx={{
                      fontSize: "1rem",
                      fontWeight: "bold",
                      borderRadius: "10px",
                      px: 3,
                      py: 1,
                    }}
                  >
                    {loading ? "Predicting..." : "Predict Price"}
                  </Button>
                </_motion.div>
              </Box>
            </form>

            {loading && (
              <Box mt={3} display="flex" justifyContent="center">
                <CircularProgress color="primary" />
              </Box>
            )}

            {predictedPrice !== null && (
              <_motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
              >
                <Paper
                  elevation={3}
                  sx={{
                    mt: 4,
                    p: 2,
                    textAlign: "center",
                    backgroundColor: "#f5f5f5",
                    borderRadius: "10px",
                    boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.2)",
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    gap: 1,
                  }}
                >
                
                  <Typography variant="h5" color="primary" fontWeight="bold">
                    Predicted Price: ₹{predictedPrice}
                  </Typography>
                </Paper>
              </_motion.div>
            )}

            {error && (
              <Typography variant="body1" color="error" align="center" mt={2}>
                {error}
              </Typography>
            )}
          </Paper>
        </_motion.div>
      </Container>
    </div>
  );
}

export default App;
