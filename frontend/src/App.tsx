import React, { useState } from 'react';
import {
  Box,
  Container,
  Typography,
  TextField,
  Button,
  Paper,
  Grid,
  List,
  ListItem,
  ListItemText,
  CircularProgress,
  Divider
} from '@mui/material';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import MovieIcon from '@mui/icons-material/Movie';
import HistoryIcon from '@mui/icons-material/History';
import axios from 'axios';

const theme = createTheme({
  palette: {
    primary: {
      main: '#000000',
    },
    background: {
      default: '#f5f5f5',
    },
  },
  typography: {
    h1: {
      fontSize: '2.5rem',
      fontWeight: 600,
    },
    h2: {
      fontSize: '1.5rem',
      fontWeight: 500,
    },
    subtitle1: {
      color: '#666',
    },
  },
});

interface AnalysisResult {
  text: string;
  sentiment: string;
  confidence: number;
  timestamp: string;
}

function App() {
  const [review, setReview] = useState('');
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState<AnalysisResult[]>([]);

  const analyzeReview = async () => {
    if (!review.trim()) return;

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8001/analyze', {
        text: review
      });

      const result: AnalysisResult = {
        text: review,
        sentiment: response.data.sentiment,
        confidence: response.data.confidence,
        timestamp: new Date().toLocaleString()
      };

      setHistory([result, ...history]);
      setReview('');
    } catch (error) {
      console.error('Error analyzing review:', error);
      // You could add error handling UI here
    } finally {
      setLoading(false);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <Box sx={{ minHeight: '100vh', bgcolor: 'background.default', py: 4 }}>
        <Container maxWidth="lg">
          <Typography variant="h1" align="center" gutterBottom>
            Movie Sentiment Analyzer
          </Typography>
          <Typography variant="subtitle1" align="center" gutterBottom>
            Analyze the sentiment of movie reviews using AI
          </Typography>

          <Grid container spacing={4} sx={{ mt: 4 }}>
            <Grid item xs={12} md={6}>
              <Paper sx={{ p: 3 }}>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <MovieIcon sx={{ mr: 1 }} />
                  <Typography variant="h2">Movie Review Analysis</Typography>
                </Box>
                <Typography variant="subtitle1" gutterBottom>
                  Enter a movie review to analyze its sentiment
                </Typography>
                <TextField
                  fullWidth
                  multiline
                  rows={4}
                  variant="outlined"
                  placeholder="Enter a movie review here..."
                  value={review}
                  onChange={(e) => setReview(e.target.value)}
                  sx={{ mb: 2 }}
                />
                <Button
                  variant="contained"
                  fullWidth
                  onClick={analyzeReview}
                  disabled={loading || !review.trim()}
                >
                  {loading ? <CircularProgress size={24} color="inherit" /> : 'Analyze Sentiment'}
                </Button>
              </Paper>
            </Grid>

            <Grid item xs={12} md={6}>
              <Paper sx={{ p: 3 }}>
                <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
                  <HistoryIcon sx={{ mr: 1 }} />
                  <Typography variant="h2">Analysis History</Typography>
                </Box>
                <Typography variant="subtitle1" gutterBottom>
                  Your recent sentiment analysis results
                </Typography>
                {history.length === 0 ? (
                  <Typography variant="body1" color="text.secondary" align="center" sx={{ py: 4 }}>
                    No analysis history yet. Analyze a review to see results here.
                  </Typography>
                ) : (
                  <List>
                    {history.map((result, index) => (
                      <React.Fragment key={index}>
                        {index > 0 && <Divider />}
                        <ListItem>
                          <ListItemText
                            primary={result.text}
                            secondary={
                              <>
                                <Typography component="span" variant="body2">
                                  Sentiment: {result.sentiment} ({(result.confidence * 100).toFixed(1)}% confidence)
                                </Typography>
                                <br />
                                <Typography component="span" variant="body2" color="text.secondary">
                                  {result.timestamp}
                                </Typography>
                              </>
                            }
                          />
                        </ListItem>
                      </React.Fragment>
                    ))}
                  </List>
                )}
              </Paper>
            </Grid>
          </Grid>
        </Container>
      </Box>
    </ThemeProvider>
  );
}

export default App; 