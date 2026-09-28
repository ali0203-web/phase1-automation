#!/bin/bash

# Disk Transfer Script - 8.5 GB to Vault
# Target: /Users/aliasgarfatepurwala/Claude-Data-Vault/archives/

VAULT_PATH="/Users/aliasgarfatepurwala/Claude-Data-Vault/archives/disk-transfer-2026-09-28"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
TRANSFER_LOG="${VAULT_PATH}/transfer_${TIMESTAMP}.log"

mkdir -p "$VAULT_PATH"

echo "========================================" | tee "$TRANSFER_LOG"
echo "DISK TRANSFER PROCESS STARTED" | tee -a "$TRANSFER_LOG"
echo "Target Vault: $VAULT_PATH" | tee -a "$TRANSFER_LOG"
echo "Timestamp: $TIMESTAMP" | tee -a "$TRANSFER_LOG"
echo "========================================" | tee -a "$TRANSFER_LOG"

# Function to copy and verify
transfer_item() {
    local SOURCE=$1
    local DEST_NAME=$2
    local DEST="${VAULT_PATH}/${DEST_NAME}"

    echo "" | tee -a "$TRANSFER_LOG"
    echo ">>> Transferring: $SOURCE" | tee -a "$TRANSFER_LOG"

    if [ -d "$SOURCE" ]; then
        echo "    Type: Directory" | tee -a "$TRANSFER_LOG"
        echo "    Size: $(du -sh "$SOURCE" | cut -f1)" | tee -a "$TRANSFER_LOG"
        cp -r "$SOURCE" "$DEST" 2>> "$TRANSFER_LOG"
        RESULT=$?
    elif [ -f "$SOURCE" ]; then
        echo "    Type: File" | tee -a "$TRANSFER_LOG"
        echo "    Size: $(du -sh "$SOURCE" | cut -f1)" | tee -a "$TRANSFER_LOG"
        cp "$SOURCE" "$DEST" 2>> "$TRANSFER_LOG"
        RESULT=$?
    else
        echo "    ERROR: Source not found" | tee -a "$TRANSFER_LOG"
        return 1
    fi

    if [ $RESULT -eq 0 ]; then
        echo "    ✅ Copied successfully" | tee -a "$TRANSFER_LOG"

        # Verify integrity
        echo "    Verifying integrity..." | tee -a "$TRANSFER_LOG"
        if [ -d "$SOURCE" ]; then
            SOURCE_SIZE=$(du -s "$SOURCE" | cut -f1)
            DEST_SIZE=$(du -s "$DEST" | cut -f1)
            if [ "$SOURCE_SIZE" = "$DEST_SIZE" ]; then
                echo "    ✅ Size verification passed" | tee -a "$TRANSFER_LOG"
                return 0
            else
                echo "    ❌ Size mismatch: $SOURCE_SIZE → $DEST_SIZE" | tee -a "$TRANSFER_LOG"
                return 1
            fi
        fi
    else
        echo "    ❌ Copy failed with code $RESULT" | tee -a "$TRANSFER_LOG"
        return 1
    fi
}

# Start transfers
echo "" | tee -a "$TRANSFER_LOG"
echo "BEGINNING TRANSFERS..." | tee -a "$TRANSFER_LOG"
echo "========================================" | tee -a "$TRANSFER_LOG"

# High Priority Items
transfer_item "$HOME/Library/Caches" "library-caches"
transfer_item "$HOME/Library/Mobile Documents" "library-mobile-docs"
transfer_item "$HOME/phase1automation" "phase1automation"
transfer_item "$HOME/agent-system" "agent-system"
transfer_item "$HOME/chatbot-env" "chatbot-env"
transfer_item "$HOME/Backups" "backups"

echo "" | tee -a "$TRANSFER_LOG"
echo "========================================" | tee -a "$TRANSFER_LOG"
echo "TRANSFER PHASE COMPLETE" | tee -a "$TRANSFER_LOG"
echo "Log saved to: $TRANSFER_LOG" | tee -a "$TRANSFER_LOG"
echo "========================================" | tee -a "$TRANSFER_LOG"

# Summary
echo "" | tee -a "$TRANSFER_LOG"
echo "VAULT CONTENTS:" | tee -a "$TRANSFER_LOG"
du -sh "$VAULT_PATH"/* 2>/dev/null | tee -a "$TRANSFER_LOG"
echo "Total transferred: $(du -sh "$VAULT_PATH" | cut -f1)" | tee -a "$TRANSFER_LOG"
